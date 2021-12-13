from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


# 템플릿(UI) 처리 views
from rest_framework.views import APIView

from accountapp.models import NewModel
from accountapp.serializers import NewModelSerializer, UserSerializer


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
    new_model_list = NewModel.objects.all()
    serializer = NewModelSerializer(new_model_list, many=True)

    return Response(serializer.data)

# Account create template Views
def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')


class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)