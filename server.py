from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c3a14b64fd3eb5f994230183700f79d1&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    return render_template('index.html', temperature=temperature, weather_desc=weather_desc)


if __name__ == '__main__':
    app.run(debug=True)
