import pytest
from unittest.mock import Mock

from fetch_weather_data import fetch_weather_data


def test_fetch_weather_data():
    # Mock the API client
    mock_api_client = Mock()

    # Mock the response from the API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": "20°C", "condition": "Sunny"}

    # Set up the mock to return the mocked response
    mock_api_client.get_weather_data.return_value = mock_response

    # Call the function to test
    result = fetch_weather_data(mock_api_client)

    # Assert that the result is as expected
    assert result == {"temperature": "20°C", "condition": "Sunny"}


def test_fetch_weather_data_failure():
    # Mock the API client
    mock_api_client = Mock()

    # Mock the response from the API to simulate a failure
    mock_response = Mock()
    mock_response.status_code = 500

    # Set up the mock to return the mocked response
    mock_api_client.get_weather_data.return_value = mock_response

    # Call the function and assert that it raises an exception
    with pytest.raises(Exception, match="Failed to fetch weather data"):
        fetch_weather_data(mock_api_client)

