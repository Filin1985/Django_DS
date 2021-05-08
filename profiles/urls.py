from django.urls import path
from .views import my_profile_view

app_name = 'profile'

urlpatterns = [
    path('', my_profile_view, name='my')
]
