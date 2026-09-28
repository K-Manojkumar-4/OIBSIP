import requests

API_key = "30227319e2104e6a1ba4f5d6f3a345bf"
base_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q" : city ,
        "appid" : API_key ,
        "units" : "metric"
    }

    try:
        response = requests.get(base_URL , params= params , timeout= 10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("City not found. Please check the spelling.")
            return None
        else:
            print("Error fetching weather data.")
            return None
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out.")
        return None
    except Exception as e:
        print("Something went wrong: " , e)
        return None

def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp_c = data["main"]["temp"]
    temp_f = (temp_c * 9/5) + 32
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].title()
    wind = data["wind"]["speed"]

    print("\n-------------------- Weather Report -------------------")
    print()
    print( f"Location       : {city} , {country} ")
    print( f"Temperature    : {temp_c :.1f}C / {temp_f :.1f}F ")
    print( f"Condition      : {description}")
    print( f"Humidity       : {humidity} % ")
    print( f"Wind           : {wind} m/s")
    print()
    print("-------------------------------------------------------\n")
print()
print("================== Basic Weather App ==================")
print()
while True:
    city = input("Enter City name (or type 'exit' to quit): ").strip()

    if city.lower() == "exit":
        print("Thanks! For more update please check the (City name) What U want")
        break
    if city == "":
        print("City name cannot be empty.")
        continue

    weather_data = get_weather(city)

    if weather_data:
        display_weather(weather_data)
