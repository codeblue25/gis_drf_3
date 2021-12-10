from django.urls import path

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView

app_name = 'accountapp'

urlpatterns = [
    # UI를 보여주는 views 라우팅
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    # 로직 처리하는 views 라우팅
    path('hello_world/', hello_world, name='hello_world'),

    # 계정 생성하는 views 라우팅
    path('create_template/', AccountCreateTemplate, name='create_template'),
    
    path('crate/', AccountCreateAPIView.as_view(), name='create'),
]