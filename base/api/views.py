from rest_framework.response import Response 
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from ..views import *
from .serializers import * 









@api_view(['GET','POST'])
def UsersList(request):
    if request.method=='GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

@api_view(['GET','POST'])
def UserDetail(request, pk):
    if request.method == 'GET':
        user = CustomUser.objects.get(id=pk) 
        serializer = CustomUserSerializer(user, many=False)
        return Response(serializer.data)

    
        

@api_view(['GET','POST'])
def ChirpList(request):
    if request.method == 'GET':
        chirps = Chirp.objects.all()
        serializer = ChirpSerializer(chirps, many=True) 
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChirpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def ChirpDetail(request,pk):
    if request.method == 'GET':
        chirp = Chirp.objects.get(id=pk)
        serializer = ChirpSerializer(chirp, many=False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ChirpSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    







class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        return Response({"message":"This is a protected view"})
    