from django.urls import path
from .views import *

urlpatterns = [
    path('', view=main, name='main'),

    path('map_view/', view=map_view, name='map_view'),
    path('map/', view=map, name='map'),
    
    path('create_user/', view=create_user, name='create_user'),
    path('login/', view= user_login, name='login'),
    path('logout/', view=user_logout, name='logout'),
]
