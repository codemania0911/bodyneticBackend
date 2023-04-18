from rest_framework import serializers
from .models import Profile, UserData, User
from rest_framework.validators import UniqueValidator


class ProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile       
        fields = '__all__'    
        
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = '__all__'
        
    
    def create(self , validated_data):
        print(validated_data)
        user = User.objects.create(email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user