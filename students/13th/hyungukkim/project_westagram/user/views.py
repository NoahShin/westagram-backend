import json
import re

from django.views import View
from django.http import JsonResponse
from user.models import Account

class SignUpView(View): #회원가입
	def post(self, request):
		data = json.loads(request.body)

		if (data['email'] == '') and (data['phone'] == ''):
			return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

		if data['password'] == '' or data['name'] == '':
			return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

		p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
		if data['email'] != '' and (p.match(str(data['email'])) != None) == False:
			return JsonResponse({'MESSAGE':'EMAIL_VALIDATION'}, status = 400)

		if Account.objects.filter(name = data['name']).exists() and (data['name'] != ''):
			return JsonResponse({'MESSAGE':'NAME_DUPLICATED'}, status = 400)
		elif Account.objects.filter(email = data['email']).exists() and (data['email'] != ''):
			return JsonResponse({'MESSAGE':'EMAIL_DUPLICATED'}, status = 400)
		elif Account.objects.filter(phone = data['phone']).exists() and (data['phone'] != ''):
			return JsonResponse({'MESSAGE':'PHONE_DUPLICATED'}, status = 400)

		if (len(data['password']) < 8):
			return JsonResponse({'MESSAGE':'PASSWORD_VALIDATION'}, status = 400)

		name = Account.objects.create(
			name = data['name'], email = data['email'], phone = data['phone'], password = data['password']
		)

		return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)

	def get(self, request):
		account_data = Account.objects.values()
		return JsonResponse({'account':list(account_data)}, status = 200)

class SignInView(View): #로그인
	def post(self, request):
		data = json.loads(request.body)
		account_data = Account.objects.values()
		name = data['name']
		email = data['email']
		phone = data['phone']
		password = data['password']

		if (email == '') and (name == '') and (phone == ''):
			return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

		if password == '':
			return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)

		if email != '' and Account.objects.filter(email = email).exists() == False:
			return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)
		elif phone != '' and Account.objects.filter(phone = phone).exists() == False:
			return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)
		elif name != '' and Account.objects.filter(name = name).exists() == False:			
			return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)

		if name != '':
			user_data = Account.objects.get(name = name)
			if user_data.password != password:
				return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)
		elif email != '':
			user_data = Account.objects.get(email = email)
			if user_data.password != password:
				return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)
		elif phone != '':
			user_data = Account.objects.get(phone = phone)
			if user_data.password != password:
				return JsonResponse({'MESSAGE':'INVALID_USER'}, status = 401)		

		return JsonResponse({'MESSAGE':'SUCCESS'}, status = 200)


	
