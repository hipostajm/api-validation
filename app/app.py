from flask import Flask
from flask import request
from views import WeatherView
from repositoryes import WeatherRepository
from controllers import WeatherController

app = Flask(__name__)

repostiory = WeatherRepository()
controller = WeatherController(repostiory)

app.add_url_rule("/", view_func=WeatherView.as_view("get smf idk", controller))