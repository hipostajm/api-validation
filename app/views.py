from flask import request
from flask.views import MethodView
from controllers import WeatherController
from controllers import BadRequest
from controllers import NotFound

class WeatherView(MethodView):
    def __init__(self, controller: WeatherController):
        super().__init__()
        self.controller = controller
    
    def get(self):
        data = request.get_json()
        
        try: 
            data = self.controller.get(data)
            return {"sucess": True, "data": data}, 200
        
        except BadRequest:
            return {"sucess": False}, 400
            
        except NotFound:
            return {"sucess": False}, 404
    
                
    def post(self):
        data = request.get_json()
        
        try:
            self.controller.add(data)
            return {"sucess": True}, 200
        
        except BadRequest:
            return {"sucess": False}, 400