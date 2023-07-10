from flask import Flask, render_template, request
import requests
from dotenv import dotenv_values
import math

app = Flask(__name__)

config = dotenv_values(".env")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = config['API']
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(weather_url)
    data = response.json()

    if data['cod'] != '404':
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        z = 10
        n = 2 ** z
        x = math.floor((lon + 180) / 360 * n)
        y = math.floor(
            (1 - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)) / math.pi) / 2 * n)
        # map_url = f'https://www.google.com/maps/place/{city}/@{lat},{lon},10z'
        icon = data['weather'][0]['icon']
        ImageURL =  f'http://openweathermap.org/img/wn/"{icon}@2x.png'
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'map_url': map_url,
            'image' : ImageURL,
        }
    else:
        weather_info = None

    return render_template('index.html', weather_info=weather_info)


if __name__ == '__main__':
    app.run(debug=True)
