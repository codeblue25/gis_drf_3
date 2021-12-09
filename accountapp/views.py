from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 템플릿(UI) 처리 view
def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리 view
@api_view()
def hello_world(request):
    return Response({'message': 'Hello JS !'})