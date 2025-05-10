command = "help"

def get_data(uuw, w):
    return True

match command.split(" "):    
        case ["help"]:
            print('owah')
            
        case ["view", date, hour]:
            print(get_data(date, int(hour)))