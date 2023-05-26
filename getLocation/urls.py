from django.urls import path
from getLocation.views import get_location, index


urlpatterns = [
    # customer site pages
    path('', index, name='index'),
    path('get_location/', get_location, name='get_location')

]