import requests
import customtkinter as ctk

def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", "").split(",")
            if len(loc) == 2:
                lat = float(loc[0])  
                long = float(loc[1])  
                return lat, long
            else:
                return None, None
        else:
            print("Błąd podczas pobierania lokalizacji użytkownika.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Błąd: {e}")
        return None, None

def get_aurora_data(lat, long):
    api_url = f"https://api.auroras.live/v1/?type=all&lat={lat}&long={long}&forecast=false&threeday=false"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()

        if "ace" in data:
            kp = data["ace"].get("kp", "brak danych")
            return f"KP: {kp}"
        else:
            return "Brak danych o zorzy polarnej."
    else:
        return "Błąd podczas pobierania danych."


def on_check_button_click():
    lat, long = get_user_location()
    
    if lat is None or long is None:
        result_label.configure(text="Nie udało się pobrać lokalizacji.")
    else:
        location_label.configure(text=f"Twoja lokalizacja: lat: {lat}, long: {long}")   
        result = get_aurora_data(lat, long)
        result_label.configure(text=result)


root = ctk.CTk()
root.title("Zorza Polarna")

city_label = ctk.CTkLabel(root, text="Sprawdzanie lokalizacji...")
city_label.pack(padx=10, pady=10)

location_label = ctk.CTkLabel(root, text="Twoja lokalizacja: lat: , long: ")
location_label.pack(padx=10, pady=10)

check_button = ctk.CTkButton(root, text="Sprawdź Zorzę", command=on_check_button_click)
check_button.pack(padx=10, pady=20)

result_label = ctk.CTkLabel(root, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()
