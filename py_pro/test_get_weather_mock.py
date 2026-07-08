import pytest

from get_weather import get_weather

def test_get_weather_success(monkeypatch):
    # Mock the requests.get method to return a successful response
    class MockResponse:
        status_code = 200
        def json(self):
            return {"temperature": "20°C", "condition": "Sunny"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = get_weather("New York")
    assert result == {"temperature": "20°C", "condition": "Sunny"}

def test_get_weather_failure(monkeypatch):
    # Mock the requests.get method to return a failure response
    class MockResponse:
        status_code = 500

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    with pytest.raises(Exception, match="Failed to fetch weather data"):
        get_weather("New York") 