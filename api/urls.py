from django.urls import path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('signup', views.RegisterApiView)
router.register('genres', views.GenreApiView)
router.register('movies', views.MovieApiView)
urlpatterns = [
    re_path(r'^login/?$', views.LoginApiView.as_view(), name='login_api')
]
urlpatterns += router.urls
