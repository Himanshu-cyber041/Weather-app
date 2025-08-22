from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "Enter here your api-key"  # Replace with your actual OpenWeatherMap API key

def get_weather_data(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather_data(city)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
