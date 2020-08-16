from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import Genre, Movie

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username',None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    msg = 'User not active.'
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Invalid credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Please enter email and password'
            raise serializers.ValidationError(msg)

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, error_messages={'required': 'First name is required'})
    last_name = serializers.CharField(required=True, error_messages={'required': 'Last name is required'})
    email = serializers.EmailField(required=True, error_messages={'required': 'Email is required'})
    password = serializers.CharField(required=True, error_messages={'required': 'Password is required'})
    username = serializers.CharField(required=True, error_messages={'required': 'Username is required'})
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        try:
            user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'],
                                            password=validated_data['password'],first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'])
            return user
        except Exception as E:
            raise serializers.ValidationError(str(E))

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre
    
class MovieSerializer(serializers.ModelSerializer):
    movie_genres = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Movie
        fields = (
            'pk',
            'name',
            'director',
            '_99_popularity',
            'imdb_score',
            'movie_genres'
        )
    
    def create(self, data):
        genres = data.pop('movie_genres')
        movie = Movie.objects.create(**data)
        for genre in genres:
            movie_genre = Genre.objects.get_or_create(name=genre.strip().title())
            movie.genre.add(movie_genre)
        return movie
    
    def update(self, instance, validated_data):
        genres = validated_data.pop('movie_genres')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.genre.clear()
        for genre in genres:
            print(genre)
            print(instance)
            movie_genre, status = Genre.objects.get_or_create(name=genre.strip().title())
            instance.genre.add(movie_genre)
        return instance
