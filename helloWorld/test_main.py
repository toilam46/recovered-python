from main import get_weather

def test_get_weather():
    assert get_weather(35) == "It's hot outside!"
    assert get_weather(25) == "It's warm outside!"
    assert get_weather(15) == "It's cool outside!"
    assert get_weather(5) == "It's cold outside!"
    