def get_weather(temperature):
    if temperature > 30:
        return "It's hot outside!"
    elif temperature > 20:
        return "It's warm outside!"
    elif temperature > 10:
        return "It's cool outside!"
    else:
        return "It's cold outside!"
    