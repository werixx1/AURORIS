import requests
import math

def get_user_location():
        try:
            response = requests.get("https://ipinfo.io/json")
            if response.status_code == 200:
                data = response.json()
                loc = data.get("loc", "").split(",")
                city = data.get("city", "Unknown city")  
                if len(loc) == 2:
                    lat = float(loc[0])  
                    long = float(loc[1])  
                    return lat, long, city
                else:
                    return None, None, city 
            else:
                print("Unable to access user's localisation")
                return None, None, "Unknown city"
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, None, "Unknown city"

def get_aurora_data(lat, long):
        api_url = f"https://api.auroras.live/v1/?type=all&lat={lat}&long={long}&forecast=false&threeday=false"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if "ace" in data:
                kp = data["ace"].get("kp", "no data")
                return kp
            else:
                return "No available information about aurora"
        else:
            return "Error while accesing data"

def haversine(lat1, lon1, lat2, lon2):
        R = 6371 
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        
        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c 