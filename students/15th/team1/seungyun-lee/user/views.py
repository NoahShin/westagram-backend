from django.shortcuts import render

# Create your views here.
import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from .models import User
from my_settings import SECRET






class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if (data['username'] == '' and data['email'] == '' and data['phonenumber'] == '') or data['password'] == '':
                raise KeyError

            if User.objects.filter(username=data['username'], email=data['email'], phonenumber=data['phonenumber'], password=data['password']).exists():
                raise ValueError

            password = data['password']
            hashed_passwords = User.objects.values_list('password', flat=True).distinct()

            for i in hashed_passwords:
                print(i)
                print(type(i))
                if bcrypt.checkpw(password.encode('utf-8'), i.encode('utf-8')):
                    raise ValueError


            if len(data['password']) < 8: #password validation
                raise ValueError 

            if 'email' in data:
                if data['email'] != '': #email validation
                    symbols_set = '@.'
                    for i in symbols_set:
                        if i not in data['email'] :
                            raise ValueError
            
            password    = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                username= data['username'], 
                email= data['email'], 
                phonenumber = data['phonenumber'], 
                password = password.decode('utf-8')
                )
            return JsonResponse({'message': 'SUCCESS'}, status = 200)
    
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except ValueError:
            return JsonResponse({'message' : 'Invalid user/password'}, status = 400)


    
    def get(self, request):
        data = json.loads(request.body)
        user_info = list(data.keys())

        try:
            if 'password' not in user_info and len(user_info) < 2:
                print('hi')
                raise KeyError

            for i in user_info:
                if i != 'password':
                    login_name = i
            
            password = data['password']
            if login_name == 'username':
                hashed_password = User.objects.get(username=data[login_name])
            elif login_name == 'email':
                hashed_password = User.objects.get(email=data[login_name])
            elif login_name == 'phonenumber':
                hashed_password = User.objects.get(phonenumber=data[login_name])
            
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.password.encode('utf-8')) == False:
                raise ValueError

            token = jwt.encode({'password' : data['password']}, SECRET, algorithm = "HS256")
            token = token.decode('utf-8')                         

            return JsonResponse({'token' : token}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except ValueError:
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)



