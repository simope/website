import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, FileResponse, JsonResponse
from django.template import loader
from .models import rps_match, user
from django.db.models import Count
import plotly.express as px
import requests
import folium


# Create your views here.

def play(request):

   # Load webpage
   template = loader.get_template('rockpaperscissors.html')

   # Extract match statistics
   data_match = (rps_match.objects
            .values('result')
            .annotate(count=Count('result'))
            .order_by())

   total = 0
   for entry in data_match:
      total += entry['count']

   for entry in data_match:
      entry['count'] /= total
      entry['count'] *= 100

   # Create bar chart
   fig = px.bar(
      data_match,
      x='result',
      y='count',
      title='RPS global statistics',
      color='result',
      labels={
         "result": '',
         "count": "Percentage of occurence %"
      }
   )

   fig.update_layout({
      'plot_bgcolor': 'rgba(0, 0, 0, 0)',
      'paper_bgcolor': 'rgba(0, 0, 0, 0)',
   })

   fig.update_layout(
      showlegend=False,
      title_x=0.5
      )

   chart = fig.to_html

   # Extract users IP already in the DB
   ip_list = list(user.objects.values_list('ip', flat=True))

   # Extract IP and locate user
   ip = request.META.get('HTTP_X_FORWARDED_FOR')
   ip = "92.109.61.185"

   ipdata = (requests.get('https://ipwho.is/'+ip)).json()

   if not(ip in ip_list):
      # Save into model and DB if not already there
      userModel = user(ip=ip, latitude=ipdata["latitude"], longitude=ipdata["longitude"])
      userModel.save()

   # Reading users locations
   data_users = (user.objects.values('latitude', 'longitude'))
   
   # Creating the users map
   f=folium.Figure(width="700px")
   m = folium.Map()
   m.add_to(f)  
   
   # Adding the markers
   for entry in data_users:
      folium.Marker(location=[entry['latitude'], entry['longitude']]).add_to(m)

   m = m._repr_html_()

   context = {'chart': chart, 'total': total, 'map': m}

   return render(request, 'rockpaperscissors.html', context)

@csrf_exempt
def save_to_DB(request):
    if request.method == 'POST':
        print(json.loads(request.body.decode()))
        result = json.loads(request.body.decode())['result']
        model = rps_match(result=result)
        model.save()
        return JsonResponse({'success': True})
  
    return JsonResponse({'success': False})


def data(request):
  form = rps_match.objects.values()
  print(form[4]['result'])
  template = loader.get_template('rockpaperscissors.html')
  return JsonResponse({'success': True})