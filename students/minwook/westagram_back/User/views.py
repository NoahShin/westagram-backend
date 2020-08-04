import json

from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError

from .models import User
# email validation
def email_format_check(email):
    if ('@' in email) and ('.' in email):
        return 0
    else:
        return 1

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            current_db = User.objects.all()
            name = data['name']
            email = data['email']
            phone = data['phone']
            password = data['password']
        except KeyError:
            return JsonResponse({'mwssage':'KEY_ERROR'}, status = 400)

        if name != '' :
            if current_db.filter(name = data['name']):
                return JsonResponse({'message':'DUPLICATE_NAME'}, status = 400)
        elif email != '' :
            if current_db.filter(email = data['email']):
                return JsonResponse({'message':'DUPLICATE_EMAIL'}, status = 400)
        elif phone != '' :
            if current_db.filter(phone = data['phone']):
                return JsonResponse({'message':'DUPLICATE_PHONE'}, status = 400)
        else:
            return JsonResponse({'message':'MINIMUM_CONDITIONS_FAILED'}, status = 400)

        if email != '':
            if email_format_check(email):
                return JsonResponse({'message':'EMAIL_FORMAT_FAILED'}, status = 400)

        if password != '':
            if len(data['password']) < 8:
                return JsonResponse({'message':'SHORT_PASSWORD'}, status = 400)
        User(
            name = name,
            password = password,
            email = email,
            phone = phone
        ).save()
        return JsonResponse({'message':'SUCCESS'}, status = 200)

    def get(self, request):
        user_data = User.objects.values()
        return JsonResponse({'users':list(user_data)}, status = 200)

"""
        target = [name, email, password, phone]

        for key in target:
            res = user_info_duplicate_check(key)

            if res == -1:
                return JsonResponse({'message':'NAME_DUPLICATE_FAILED'}, status = 400)
            elif res == -2:
                return JsonResponse({'message':'EMAIL_DUPLICATE_FAILED'}, status = 400)
            elif res == -3:
                return JsonResponse({'message':'PHONE_DUPLICATE_FAILED'}, status = 400)

            return JsonResponse({'message':'who sad'}, status = 400)
"""
