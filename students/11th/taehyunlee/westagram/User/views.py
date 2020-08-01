import json

from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError

from .models import User

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if '@' and '.' not in data['email']:
                return JsonResponse(
                    {"message":"Email_Not_Verified"},
                    status = 404
                )
            elif len(data['password']) < 8:
                return JsonResponse(
                    {"message":"Password_Not_Verified"},
                    status = 411
                )
            else:
                User(
                    name     = data['name'],
                    email    = data['email'],
                    phone    = data['phone'],
                    password = data['password']
                ).save()
                return JsonResponse(
                    {"message":"SUCCESS"},
                    status = 200
                )
        except IntegrityError:
            return JsonResponse(
                {"message":"Data_Already_Exists"},
                status = 409
            )
        except KeyError:
            return JsonResponse(
                {"message":"KEY_ERROR"},
                status = 400
            )
