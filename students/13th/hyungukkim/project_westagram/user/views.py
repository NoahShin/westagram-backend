import json

from django.views import View
from user.models import Account

class UserView(View):
	def post(self, request):
		data = json.load(requests.body)
		
		name = Account.objects.create(name=data['name'])
		email = Account.objects.create(email=data['email'])
		phone = Account.objects.create(phone=data['phone'])
		password = Account.objects.create(password=data['password'])

		return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
