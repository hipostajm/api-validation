from flask import Flask
from flask import request
from AppView import AppView
from AppRepository import AppRepository

app = Flask(__name__)

appRepository = AppRepository() 
appView = AppView(appRepository=appRepository)
         