from django.http import HttpResponse
from django.template import loader
import requests
from game.models import user

def home(request):
  template = loader.get_template('home.html')
  ############################################
  ############################################
  # IP extraction

  # Extract users IP already in the DB
  ip_list = list(user.objects.values_list('ip', flat=True))

  # Extract IP and locate user
  #ip = request.META.get('HTTP_X_FORWARDED_FOR')
  #ip = ip.split(', ')[0]
  ip = "92.109.61.185"

  ipdata = (requests.get('https://ipwho.is/'+ip)).json()

  if not(ip in ip_list):
    # Save into model and DB if not already there
    userModel = user(ip=ip, name="No name", latitude=ipdata["latitude"], longitude=ipdata["longitude"], points=0)
    userModel.save()

  return HttpResponse(template.render())


