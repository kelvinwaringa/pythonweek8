import requests
from django.shortcuts import render
API_KEY = " "   # Replace with your actual API key

def home(request):
    weather_data = None
    city = request.GET.get('city', '')  # Get the city from the query parameter
    
    if city:

        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}
        except requests.exceptions.RequestException as e:
            weather_data = {'error': 'Failed to connect to the weather service.'}
    
    context = {'weather_data': weather_data, 'city': city}
    return render(request, 'weather/home.html', context)
