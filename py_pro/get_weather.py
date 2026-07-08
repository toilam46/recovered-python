import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/data?city={city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch weather data") 