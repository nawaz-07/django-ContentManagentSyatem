from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cms_app.serializers import UserSignupSerializer, UserLoginSerializer, ContentItemSerializer
from cms_app.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from cms_app.models import CustomUser, ContentItem   
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAdminOrAuthorOrReadOnly

# from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSignupView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg' : 'Register Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = CustomUser.objects.filter(email=email, password=password).first()
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'}, status = status.HTTP_200_OK)
            else:
                return Response({'errrors':{'non_field_errors':['Email or Password is not valid']}}, status = status.HTTP_404_NOT_FOUND)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentItemListCreateView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        global serializer
        user = request.data
        existing_info = ContentItem.objects.filter(title=user["title"])
        if existing_info:
            return Response({'message': 'Information already exists for the user'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ContentItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(**user)
            return Response({'message': 'Content created successfully'}, status=status.HTTP_201_CREATED)
        return Response( {'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        