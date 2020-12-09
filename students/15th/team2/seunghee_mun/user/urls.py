from django.urls import path
from user.views import UserView, SigninView
 # 같은 디렉토리에 있는 views.py 파일을 불러옴.

urlpatterns = [
	path('', UserView.as_view()),
        path('signin', SigninView.as_view()),
]
