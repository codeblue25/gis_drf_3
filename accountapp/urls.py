from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, \
    AccountLoginView, AccountRetrieveAPIView

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
    path('create/', AccountCreateAPIView.as_view(), name='create'),

    path('retrieve/<int:pk>', AccountRetrieveAPIView.as_view(), name='retrieve'),
]