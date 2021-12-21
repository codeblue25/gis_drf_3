from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, \
    AccountLoginView, AccountRetrieveTemplateView, AccountUpdateTemplateView, AccountDestroyTemplateView, \
    AccountRUDAPIView, AccountTokenRetrieveAPIView

app_name = 'accountapp'

urlpatterns = [
    # UI를 보여주는 views 라우팅
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    # 로직 처리하는 views 라우팅
    path('hello_world/', hello_world, name='hello_world'),

    # 로그인, 로그아웃 views 라우팅
    path('login_template/', AccountLoginView, name='login_template'),
    path('login/', views.obtain_auth_token, name='login'),
    path('logout_template/', TemplateView.as_view(template_name='accountapp/logout.html'), name='logout_template'),

    # 계정 생성하는 views 라우팅
    path('create_template/', AccountCreateTemplate, name='create_template'),
    path('', AccountCreateAPIView.as_view(), name='create'),

    # 유저 정보 조회, 업데이트, 삭제하는 template 라우팅
    path('retrieve_template/<int:pk>', AccountRetrieveTemplateView.as_view(), name='retrieve_template'),
    path('update_template/<int:pk>', AccountUpdateTemplateView.as_view(), name='update_template'),
    path('delete_template/<int:pk>', AccountDestroyTemplateView.as_view(), name='delete_template'),
    # 유저 정보 조회, 업데이트, 삭제하는 Views 라우팅
    path('<int:pk>', AccountRUDAPIView.as_view(), name='RUD'),

    path('token/', AccountTokenRetrieveAPIView.as_view(), name='token'),
]

"""
ListCreateAPIView
127.0.0.1:9000/accounts  + HTTP method + GET = LIST  => 지금 당장 필요 없음
127.0.0.1:9000/accounts  + HTTP method + POST = Create

RetrieveUpdateDestroyAPIView
127.0.0.1:9000/accounts/1  + HTTP method + GET = Detail
127.0.0.1:9000/accounts/1  + HTTP method + PUT / PATCH  = Update
127.0.0.1:9000/accounts/1  + HTTP method + DELETE = Delete
"""