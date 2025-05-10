from flask import request
from flask.views import View
from AppRepository import AppRepository

class AppView(View):
    def __init__(self, appRepository: AppRepository):
        super().__init__()
        self.repository = appRepository
    
    def save_record(self):
        ...
    
    def _validate_data(self, data):
        ...
    
    def get_record(self, id):
        ...