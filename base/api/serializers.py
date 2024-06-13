from rest_framework import serializers 
from ..models import *

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser 
        fields = ['id','username','email']

    

class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chirp 
        fields = ['id','chirp','author','created'] 


    