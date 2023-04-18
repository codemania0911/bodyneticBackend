from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, UserData
from .serializers import ProfileSerializer, UserDataSerializer

# Create your views here.

class ProfileList(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        print(queryset)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileDetail(APIView):
    
    def get_object(self, pk):
        profile = get_object_or_404(Profile, pk=pk)
        return profile
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserDataList(APIView):
    def get(self, request):
        queryset = UserData.objects.all()
        print(queryset)
        serializer = UserDataSerializer(queryset, many=True)
        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserDataDetail(APIView):
    
    def get_object(self, pk):
        userdata = get_object_or_404(UserData, pk=pk)
        return userdata
    
    def get(self, request, pk):
        userdata = self.get_object(pk)
        serializer = UserDataSerializer(userdata)
        return Response(serializer.data)
    
    def put(self, request, pk):
        userdata = self.get_object(pk)
        serializer = UserDataSerializer(userdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        userdata = self.get_object(pk)
        userdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)