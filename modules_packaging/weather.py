import requests

API_KEY = "5a57d35d12af455795c201418250606"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

location = "Nairobi"

url = f"{BASE_URL}?key={API_KEY}&q={location}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()


    location_name = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]


    print(f"Weather in {location_name}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError:
    print("Unexpected response format.")
