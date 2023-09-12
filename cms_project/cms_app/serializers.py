from rest_framework import serializers
from .models import CustomUser, ContentItem

class UserSignupSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type':'password2'},write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'fullname','password','phone', 'address', 'city', 'state', 'country', 'pincode']
def create(self):
    return CustomUser.objects.create_user(**validated_data)    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'
