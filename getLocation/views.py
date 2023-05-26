import json
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from geopy.geocoders import Nominatim
from shapely import from_geojson,contains, Point

# Create your views here.
def index(request):
    return render(request,'index.html')

def get_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(latitude,longitude)
        # calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")

        # co-ordinates of user from the browser console
        location = loc.reverse((latitude,longitude)) #change according to the output on console
        print(location.address)
        # Return a JSON response to indicate success
        response_data = {'message': 'Coordinates received successfully', 'address':location.address}
        return JsonResponse(response_data)

    # Return a JSON response to indicate failure
    response_data = {'message': 'Invalid request'}
    return JsonResponse(response_data, status=400)
