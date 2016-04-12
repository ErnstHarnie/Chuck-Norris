from django.shortcuts import render
from django.http import HttpResponse
from chuck_norris.forms import PostForm
import urllib2 as ur
from urllib2 import urlopen
import json

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
# Create your views here.

def index(request):
	return render(request, 'chuck_norris/index.html', {})

def joke(request):
	joke = ''
	form = request.user
	voornaam = request.POST.get("voornaam", "")
	achternaam = request.POST.get("achternaam", "")
	naam = voornaam = achternaam
	url = ''
	if not r.exists(naam):
		urlString = str('http://api.icndb.com/jokes/random?firstName=John' + voornaam + '&lastName=' + achternaam)					# create url
		response = ur.urlopen(urlString).read() 
		result = json.loads(response.decode('utf-8'))		
    									# else
		r.set(naam, json.dumps(joke))			
	else:													
		response = r.get(naam)						
		joke = json.loads(response.decode('utf-8'))		
	return render(request, 'chuck_norris/joke.html', {'joke': joke})