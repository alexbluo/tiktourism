from django.contrib.gis.geoip2 import GeoIP2
from tikrest.models import Restaurant
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from decouple import config
import geopy.distance
import requests
import time

def index(request):
    API_KEY = config('GOOGLE_API')

    context = {}

    g = GeoIP2() 
    ip = request.META.get('REMOTE_ADDR', None)
    lat,lng = g.lat_lon("192.206.151.131")
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "%2C" + str(lng) + "&radius=1500&type=restaurant&key=" + API_KEY

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    for place in response.json()["results"]:
        name = place["name"]
        rating = place["rating"]
        try:
            loc = Restaurant.objects.get(name=name, rating=rating)
        except Restaurant.DoesNotExist:
            loclat = place["geometry"]["location"]["lat"]
            loclng = place["geometry"]["location"]["lng"]
            prox = geopy.distance.geodesic((lat,lng), (loclat, loclng)).mi
            mil = True;
            if (prox * 2252 <= 1000):
                prox = prox * 2252
                mil = False
            else:
                prox = round(prox, 3)
            element = place["photos"][0]["photo_reference"]
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference=" + element + "&key=" + API_KEY

            payload={}
            headers = {}

            imageResponse = requests.request("GET", photo_url, headers=headers, data=payload)
            loc = Restaurant(name=name, rating=rating, image=imageResponse.url, time_spent=0.0, proximity=prox, prox_mi=mil, liked=False, clicked=False)
            loc.save()

    restaurants = Restaurant.objects.all().values()
    context = {
        "restaurants": restaurants,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def updaterecord(request, name):
    time = request.POST['time']
    member = Restaurant.objects.get(name=name)
    member.time_spent = time + member.time_spent
    member.save()
    return HttpResponseRedirect(reverse('index'))