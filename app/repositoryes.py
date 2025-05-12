from datetime import datetime

class Record():
    def __init__(self, date: datetime,temperature: float, rain: float, apparent_temperature: float, pressure: float):
        self.date = date
        self.temperature = temperature
        self.rain = rain
        self.apparent_temperature = apparent_temperature
        self.pressure = pressure

    def __eq__(self, value):
        if isinstance(value, Record):
            return self.date == value.date
        
        if isinstance(value, datetime):
            return self.date == value
        
        raise NotImplemented
        
    def __gt__(self, value):
        if isinstance(value, Record):
            return self.date > value.date
        
        if isinstance(value, datetime):
            return self.date > value
            
        raise NotImplemented
    
    def __lt__(self, value):
        if isinstance(value, Record):
            return self.date < value.date
        
        if isinstance(value, datetime):
            return self.date < value
            
        raise NotImplemented
    
    def __le__(self, value):
        if isinstance(value, Record):
            return self.date <= value.date
        
        if isinstance(value, datetime):
            return self.date <= value
            
        raise NotImplemented

    def __ge__(self, value):
        if isinstance(value, Record):
            return self.date >= value.date
        
        if isinstance(value, datetime):
            return self.date >= value
            
        raise NotImplemented
    
    
    
class WeatherRepository():
    def __init__(self):
        self.records: list[Record] = []
    
    def add(self, record: Record) -> None:
        self.records.append(record)
        
    def get_all(self) -> list[Record]:
        return self.records
        
    def get(self, id: int) -> Record:
        return self.records[id]