from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import LoginSerializer, RegisterSerializer, GenreSerializer, MovieSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Genre, Movie
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from api.permission_classes import CheckPermission
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class LoginApiView(APIView):
    http_method_names = ('post', )
    def post(self, request):
        data = LoginSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        user = data.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'success': True,
            'token': token.key
        })

class RegisterApiView(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ('post', )
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'success': True,
            'message': 'Sign up successfull'
        }, status=status.HTTP_201_CREATED, headers=headers)

class GenreApiView(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (CheckPermission, )
    filter_backends = (SearchFilter, OrderingFilter)

    ordering_fields = ('created_on', 'name')
    search_fields = ('name', )


class MovieApiView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (CheckPermission, )
    filter_backends = (SearchFilter, OrderingFilter)

    ordering_fields = ('created_on', 'director', 'name', '_99_popularity', 'imdb_score')
    search_fields = ('name', 'director')
