from rest_framework import serializers
from .models import Profile, UserData

class ProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile       
        fields = '__all__'    
        
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'