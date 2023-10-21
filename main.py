import requests

api_key = "1fcbb3d2c2163d5e91bd1f924c0b6de5"

base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter your city name: ")

complete_url = f"{base_url}q={city_name}&appid={api_key}"

response = requests.get(complete_url)
data = response.json()

if data["cod"] == 200:
    print("Current Temperature:", data["main"]["temp"])
    print("Current Temperature Feels Like:", data["main"]["feels_like"])
    print("Maximum Temperature:", data["main"]["temp_max"])
    print("Minimum Temperature:", data["main"]["temp_min"])
else:
    print(f"City not found or there was an issue with the request. Status code: {data['cod']}")
