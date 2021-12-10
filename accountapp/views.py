from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 템플릿(UI) 처리 views
from accountapp.models import NewModel
from accountapp.serializers import NewModelSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리 views
@api_view(['GET', 'POST'])
def hello_world(request):

    # POST
    if request.method == 'POST':
        input_data = request.data.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        # Serialize
        serializer = NewModelSerializer(new_model)

        return Response(serializer.data)

    # GET
    return Response({'message': 'Return Text'})