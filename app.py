import requests
import argparse

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'368593cfa794957aa4559f5e77197fe7'}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print_weather_data(data)
    else:
        print("Error with code:", response.status_code)

def print_weather_data(data):
    print("weather:",data['weather'][0]['description'])
    print("temperature:",data['main']['temp'])
    print("pressure:",data['main']['pressure'])
    print("humidity:",data['main']['humidity'])
    print("Wind Speed",data['wind']['speed'])
    print("Minimum Temperature",data['main']['temp_min'])
    print("Maximum Temperature",data['main']['temp_max'])
    print("rainfall",data['rain']['1h'])

   


parser = argparse.ArgumentParser()
parser.add_argument("city", help="Enter a city name")
args = parser.parse_args()    
city = args.city
get_weather(city)


