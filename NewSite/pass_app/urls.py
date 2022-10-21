from django.urls import path
from . import pass_views

# TEMPLATE URLS!
app_name = 'pass_app'

urlpatterns = [
    path('registration/', pass_views.register, name='register'),
    path('special/', pass_views.special, name='special'),
    path('login/', pass_views.user_login, name='user_login')
]
