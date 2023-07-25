
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = '368593cfa794957aa4559f5e77197fe7'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return render_template('weather_result.html', weather_data=weather_data)
    else:
        return render_template('home.html', error='City not found.')

if __name__ == '__main__':
    app.run(debug=True)
