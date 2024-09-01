from django.urls import path
from .views import *

urlpatterns = [
    path('', view=main, name='main'),
    path('map/', view=map, name='map'),
    path('create_user/', view=create_user, name='create_user'),
]