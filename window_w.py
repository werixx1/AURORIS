import customtkinter as ctk
import webbrowser
from PIL import Image
import requests
import math

class Auroris(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AURORIS")
        self.geometry("900x600")
        self.resizable(False, False)
        self.bg_image = ctk.CTkImage(Image.open("new1.png"), size=(900, 600))
        self.bg_image_label = ctk.CTkLabel(self, text="", image=self.bg_image)
        self.bg_image_label.pack(fill="both", expand=True)

        self.start_button = ctk.CTkButton(self, text="start", 
                                          command=self.on_check_button_click, 
                                          width=170,  
                                          height=55,  
                                          fg_color="#BF3EF0",
                                          hover_color="#7F3EF0",
                                          font=("Verdana", 25),
                                          corner_radius=15)
        self.start_button.place(x=78, y=379)

        self.result_label = ctk.CTkLabel(self, 
                                         text="",
                                         fg_color="#1B0420", 
                                         font=("Yu Gothic Medium", 17))
        self.result_label.place(x=529, y=177)

        self.location_label = ctk.CTkLabel(self, 
                                           text="", 
                                           fg_color="#1B0420",
                                           font=("Lucida Console", 20))
        self.location_label.place(x=529, y=177)

        self.kp_label = ctk.CTkLabel(self, 
                                     text="",
                                     fg_color="#1B0420",
                                     font=("Lucida Console", 20))
        self.kp_label.place(x=421, y=240)

        self.no_aurora = ctk.CTkLabel(self, 
                                      text="",
                                      fg_color="#1B0420",
                                      font=("Lucida Console", 20))
        self.no_aurora.place(x=443, y=288)

        self.closest_location_label = ctk.CTkLabel(self, 
                                                   text="",
                                                   fg_color="#1B0420",
                                                   font=("Lucida Console", 20))
        self.closest_location_label.place(x=464, y=382)

        self.open_link_button = ctk.CTkButton(self, 
                                              text="Watch live", 
                                              state="disabled",
                                              fg_color="#BF3EF0",
                                              hover_color="#7F3EF0",
                                              width=100,  
                                              height=40,
                                              font=("Verdana", 19))
        self.open_link_button.place(x=553, y=427)

        # Przyciski dodatkowe
        self.create_static_buttons()

    def create_static_buttons(self):
        def github_open():
            webbrowser.open("https://github.com/werixx1/AURORIS")
        
        def show_resources_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("Resources")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="Resources links:", 
                                        font=("Verdana", 13))
            label.pack(pady=10)

            link1_button = ctk.CTkButton(popup, text="Aurora API", 
                                         command=lambda: webbrowser.open("http://auroraslive.io/#/api/v1/all"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link1_button.pack(pady=5)

            link2_button = ctk.CTkButton(popup, text="IP API", 
                                         command=lambda: webbrowser.open("https://ipinfo.io/"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link2_button.pack(pady=5)

            link3_button = ctk.CTkButton(popup, text="Documentation", 
                                         command=lambda: webbrowser.open("https://github.com/TomSchimansky/CustomTkinter"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link3_button.pack(pady=5)

        def show_how_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("How does it work")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="This is how the app works\nI know what I do\ndon't panic", font=("Verdana", 13))
            label.pack(pady=50)

        def show_live_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("Live transmissions")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="Choose a place to see \na live aurora transmission from:", font=("Verdana", 12))
            label.pack(pady=10)

            link1_button = ctk.CTkButton(popup, text="Fairbanks, AK", 
                                         command=lambda: webbrowser.open("https://explore.org/livecams/UAF/aurora-cam"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link1_button.pack(pady=4)

            link2_button = ctk.CTkButton(popup, text="Vorkuta, Russia",
                                          command=lambda: webbrowser.open("https://starvisor.net/vrkt/"),
                                          fg_color="#BF3EF0",
                                          hover_color="#7F3EF0")
            link2_button.pack(pady=4)

            link3_button = ctk.CTkButton(popup, text="Rotstund, Norway", 
                                         command=lambda: webbrowser.open("https://lyngen-north.com/aurora-borealis-live-cam"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link3_button.pack(pady=4)

            link4_button = ctk.CTkButton(popup, text="Abisko, Sweden", 
                                         command=lambda: webbrowser.open("https://lightsoverlapland.com/aurora-webcam/"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link4_button.pack(pady=4)

        self.resources_button = ctk.CTkButton(self, text="Resources", 
                                              command=show_resources_popup, 
                                              width=70,  
                                              height=30,  
                                              fg_color="#3B0B46",
                                              hover_color="#6FF1FF",
                                              font=("Verdana", 14), 
                                              text_color="#838383")
        self.resources_button.place(x=60, y=9)

        self.how_button = ctk.CTkButton(self, text="How does it work", 
                                         command=show_how_popup, 
                                         width=70,  
                                         height=30,  
                                         fg_color="#3B0B46",
                                         hover_color="#6FF1FF",
                                         font=("Verdana", 14), 
                                         text_color="#838383")
        self.how_button.place(x=160, y=10)

        self.live_button = ctk.CTkButton(self, text="Live transmissions", 
                                          command=show_live_popup, 
                                          width=70,  
                                          height=30,  
                                          fg_color="#3B0B46",
                                          hover_color="#6FF1FF",
                                          font=("Verdana", 14), 
                                          text_color="#838383")
        self.live_button.place(x=310, y=10)

        github_image = ctk.CTkImage(Image.open("git.png"), size=(25, 25))
        self.github_button = ctk.CTkButton(self, text="", 
                                           image=github_image,
                                           command=github_open, 
                                           width=25,  
                                           height=25,  
                                           fg_color="#1B1F23",
                                           hover_color="#6FF1FF")
        self.github_button.place(x=10, y=6)

    def on_check_button_click(self):
        lat, long, city = self.get_user_location()
        
        if lat is None or long is None:
            self.result_label.configure(text="Failed to retrieve location")
        else:
            self.location_label.configure(text=f"{city}\nlat: {lat}\n long: {long}")   
            kp = self.get_aurora_data(lat, long)
        
        if kp == "no data" or kp == "Error while accesing data": 
            self.kp_label.configure(text="No information available")
        else:
            self.kp_label.configure(text=f"{kp}")

        if isinstance(kp, str) or float(kp) < 5:
            self.no_aurora.configure(text=f"Aurora is not visible in your area.")
            locations = [
                {"name": "Fairbanks, AK", "lat": 64.8378, "long": -147.7164, "link": "https://explore.org/livecams/UAF/aurora-cam"},
                {"name": "Vorkuta, Russia", "lat": 67.5000, "long": 64.0000, "link": "https://starvisor.net/vrkt/"},
                {"name": "Rotstund, Norway", "lat": 69.0833, "long": 19.1500, "link": "https://lyngen-north.com/aurora-borealis-live-cam"},
                {"name": "Abisko, Sweden", "lat": 68.3531, "long": 18.8350, "link": "https://lightsoverlapland.com/aurora-webcam/"}
            ]
            
            closest_location = None
            min_distance = float('inf')
            for location in locations:
                distance = self.haversine(lat, long, location["lat"], location["long"])
                if distance < min_distance:
                    min_distance = distance
                    closest_location = location
            
            self.closest_location_label.configure(text=f"{closest_location['name']} ({min_distance:.2f} km)")
            
            self.open_link_button.configure(state="normal")
            
            def open_live_stream():
                webbrowser.open(closest_location['link'])

            self.open_link_button.configure(command=open_live_stream)

    def get_user_location(self):
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

    def get_aurora_data(self, lat, long):
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

    def haversine(self, lat1, lon1, lat2, lon2):
            R = 6371 
            phi1 = math.radians(lat1)
            phi2 = math.radians(lat2)
            delta_phi = math.radians(lat2 - lat1)
            delta_lambda = math.radians(lon2 - lon1)
            
            a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            
            return R * c 

if __name__ == "__main__":
    app = Auroris()
    app.mainloop()
