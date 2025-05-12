import openmeteo_requests
import requests_cache
from retry_requests import retry
import requests

cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
url = "https://archive-api.open-meteo.com/v1/archive"


def get_data(date: str, hour: int) -> dict:
    params = {
        "latitude": 52.2298,
        "longitude": 21.0118,
        "start_date": date,
        "end_date": date,
        "hourly": ["temperature_2m", "rain", "apparent_temperature", "surface_pressure"]
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    return {
            "temperature": float(hourly.Variables(0).ValuesAsNumpy()[hour]),
            "rain": float(hourly.Variables(1).ValuesAsNumpy()[hour]), 
            "apparent temperature": float(hourly.Variables(2).ValuesAsNumpy()[hour]), 
            "pressure": float(hourly.Variables(3).ValuesAsNumpy()[hour])
    }

IP = "http://127.0.0.1:5000"

while True:
    command = input("> ")
    
    match command.split(" "):    
            case ["help", *args]:
                print("""view [date] [hour] -> prints weather info in specific day and hour
save [date] [hour] -> sends data to backend which is then saved on it
get [date] [hour] -> gives you the nearest date which was saved on backend
help -> this thing
quit -> quits""")
                
            case ["quit", *args]:
                break
            
            case ["view", date, hour]:
                data = get_data(date, int(hour)) 
                for k, v in data.items():
                    print(f"{k}: {v}")
            
            case ["save", date, hour]:
                data = get_data(date, int(hour))
                for k, v in data.items():
                    print(f"{k}: {v}")
                    
                data.update({"date": date, "hour": int(hour)})
                
                response = requests.post(url=IP+"/", json=data)            
                
                print(f"sucess: {response.json()["sucess"]}")
                
            case ["get", date, hour]:
                response = requests.get(url=IP+"/", json = {"date": date, "hour": int(hour)})
                
                if response.json()["sucess"]:
                    data = response.json()["data"]
                    for k, v in data.items():
                        print(f"{k}: {v}")
                else:
                    print("idk smf happend")
            
        