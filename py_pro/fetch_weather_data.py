def fetch_weather_data(api_client):
    response = api_client.get_weather_data("https://api.weather.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch weather data")
    