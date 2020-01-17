from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from schoolease_users.api.serializers import RegistrationSerializer, GetUsers
from schoolease_users.models import Account

@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfully registered a new user"
        data['email'] = account.email
        data['username'] = account.username
        data['category'] = account.category
    else:
        data = serializer.errors
    return Response(data)

@api_view(['GET',])
def getuser_view(request,slug):
    try:
        user_details = Account.objects.get(email=slug)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={"Http_404_error: no data has found on this email id"})
    if request.method == 'GET':
        serializer = GetUsers(user_details)
        return Response(serializer.data)

@api_view(['PUT',])
def edituser_view(request,slug):
    try:
        user_details = Account.objects.get(email=slug)

    except Account.DoesNotExist:
        return Response(data={"Http_404_error: no data has found on this email id"},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = GetUsers(user_details,data=request.data,partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)