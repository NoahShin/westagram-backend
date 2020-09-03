import json
import re
from django.views import View
from django.http  import JsonResponse
from .models      import Users


class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        Users(
            email           = data['email'],
            password        = data['password']
        ).save()

        # 회원가입시 휴대폰번호와 이메일 중 이메일을 사용할 경우 전달이 안되었을 때 에러 반환
        if not Users.objects.filter(email=email) == True:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
   
        # 회원가입시 이메일을 사용할 경우 @ 과 . 이 포함 안된경우 에러 반환
        # if Users.email.filter(r'[^@.]$') == True:     
        if not (Users.objects.get(email__contains='@') or Users.objects.get(email__contains='.')) == True:
        # shell 에서는 정상 작동 하는데 여기서는 안되네요.. 이미 저장된 정보만 가지고 할 수 있는 메소드 일까요?ㅠㅠ
            return JsonResponse({'message': 'Incorrect format'}, status=400)    # 에러 반환 

        # 아이디(이메일)가 중복된 경우 에러 반환
        if Users.objects.filter('email'==data['email']).exists() == True:
            return JsonResponse({'message': 'Already Exist'}, status=409)    # 에러 반환
        
        # 비밀번호 전달이 안된 경우
        if not Users.objects.filter(password=password) == True:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        # 비밀번호가 8자리 미만일 경우 에러 반환
        if Users.password.filter(r'\d{,7}$') == True:
        # if Users.objects.filter(password__range(8)) == True:
        # 이게 더 맞을지...
            return JsonResponse({'message': 'Too short'}, status=400)   # 에러 반환



        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users': list(user_data)}, status=200)
