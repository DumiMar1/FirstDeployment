from django.urls import path
from . import site_views


# TEMPLATE TAGGING
app_name = 'new_site_app'


urlpatterns = [
    path('relative/', site_views.relative, name='relative'),
    path('other/', site_views.other, name='other')
]

