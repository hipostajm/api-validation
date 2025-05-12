from repositoryes import WeatherRepository
from repositoryes import Record
from datetime import datetime

class BadRequest(Exception):
    pass

class NotFound(Exception):
    pass

class WeatherController():
    def __init__(self, repository: WeatherRepository):
        self._repository = repository
    
    def add(self, data: dict):
        self._validate_data(data)
        date = datetime.fromisoformat(f"{data["date"]} 0{data["hour"]}") if data["hour"] < 10 else datetime.fromisoformat(f"{data["date"]} {data["hour"]}")
        
        if date in self._repository.get_all():
            raise BadRequest
        
        rain = data["rain"]
        temperature = data["temperature"]
        apparent_temperature = data["apparent temperature"]        
        pressure = data["pressure"]
        
        record = Record(date, temperature, rain, apparent_temperature, pressure)
        
        self._repository.add(record)
    
    def get(self, data: dict):
        self._validate_date(data["date"])
        self._validate_hour(data["hour"])
        
        all_record = self._repository.get_all()
        
        if all_record == []:
            raise NotFound
        
        nearest_record = all_record[0]
        
        date = datetime.fromisoformat(f"{data["date"]} 0{data["hour"]}") if data["hour"] < 10 else datetime.fromisoformat(f"{data["date"]} {data["hour"]}")
        
        for record in all_record[1:]:
            if abs(nearest_record.date - date) > abs(record.date - date):
                nearest_record = record
                
        map_data = {"date": str(nearest_record.date.date()), 
                    "hour": int(nearest_record.date.hour), 
                    "temperature": nearest_record.temperature, 
                    "apparent temperature": nearest_record.apparent_temperature, 
                    "pressure": nearest_record.pressure,
                    "rain": nearest_record.rain}
        
        return map_data
        
    def _validate_data(self, data: dict):
        if set(data.keys()) != {"hour", "date", "rain", "temperature", "apparent temperature", "pressure"}:
            raise BadRequest
            
        hour = data["hour"]
        date = data["date"]
        rain = data["rain"]
        temperature = data["temperature"]
        apparent_temperature = data["apparent temperature"]
        pressure = data["pressure"]
        
        self._validate_date(date)
        self._validate_hour(hour)
        self._validate_rain(rain)
        self._validate_temperature(temperature)
        self._validate_apparent_temperature(apparent_temperature, temperature)
        self._validate_pressure(pressure)
        
    def _validate_date(self, date):
        if not isinstance(date, str):
            raise BadRequest
        
        try:
            datetime.fromisoformat(date)
        except:
            raise BadRequest
        
    def _validate_hour(self, hour):
        if not isinstance(hour, int) and hour not in range(0, 23+1):
            raise BadRequest
        
    def _validate_apparent_temperature(self, apparent_temperature, temperature):
        if not isinstance(apparent_temperature, int|float) and apparent_temperature not in range(temperature-10, temperature+10+1):
            raise BadRequest
    
    def _validate_temperature(self, temperature):
        if not isinstance(temperature, int|float) and temperature not in range(-20, 42+1):
            raise BadRequest
    
    def _validate_rain(self, rain):
        if not isinstance(rain, int|float) and rain < 0:
            raise BadRequest
        
    def _validate_pressure(self, pressure):
        if not isinstance(pressure, int|float) and pressure not in range(970, 1040+1):
            raise BadRequest
        
        
        