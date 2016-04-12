from django.shortcuts import render
from django.http import HttpResponse
import urllib2 as ur
from urllib2 import urlopen
import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def index(request):
	return render(request, 'chuck_norris/index.html', {})

def joke(request):
	joke = ''
	form = request.user
	voornaam = request.POST['voornaam']
	achternaam = request.POST['achternaam']
	naam = voornaam + achternaam

	if not r.exists(naam):
		urlString = str('http://api.icndb.com/jokes/random?firstName=' + voornaam + '&lastName=' + achternaam)					# create url
		response = ur.urlopen(urlString).read() 
		joke = json.loads(response.decode('utf-8'))		
		r.set(naam, json.dumps(joke))			
	else:													
		response = r.get(naam)						
		joke = json.loads(response.decode('utf-8'))		
	return render(request, 'chuck_norris/joke.html', {'joke': joke['value']['joke']})