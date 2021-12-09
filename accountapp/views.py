from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 템플릿(UI) 처리 views
def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리 views
@api_view(['GET', 'POST'])
def hello_world(request):

    # POST
    if request.method == 'POST':
        input_data = request.data.get('input_data')
        return Response({'message': input_data})

    # GET
    return Response({'message': 'Return Text'})