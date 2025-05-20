import requests

API_KEY = "4923e13f9d3c65e7b9276ca3c2ff409b"  # substitua pela sua chave
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'en'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        return {
            'City': data['name'],
            'Weather': data['main']['temp'],
            'Description': data['weather'][0]['description']
        }
    else:
        return {'erro': 'Cidade não encontrada'}


print(get_weather("Tokyo"))