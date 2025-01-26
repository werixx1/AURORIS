import customtkinter as ctk
import webbrowser
from PIL import Image
import webview 
from src.logic import get_user_location, get_aurora_data, haversine

class Auroris(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AURORIS")
        self.geometry("900x600")
        self.resizable(False, False)
        self.bg_image = ctk.CTkImage(Image.open("AURORIS/src/imgs/background.png"), size=(900, 600))
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
                                         font=("Cascadia Code Light", 20))
        self.result_label.place(x=529, y=170)

        self.location_label = ctk.CTkLabel(self, 
                                           text="", 
                                           fg_color="#26092F",
                                           font=("Cascadia Code Light", 20))
        self.location_label.place(x=529, y=170)

        self.kp_label = ctk.CTkLabel(self, 
                                     text="",
                                     fg_color="#26092F",
                                     font=("Cascadia Code Light", 20))
        self.kp_label.place(x=421, y=237)

        self.no_aurora = ctk.CTkLabel(self, 
                                      text="",
                                      fg_color="#26092F",
                                      font=("Cascadia Code Light", 20))
        self.no_aurora.place(x=443, y=281)

        self.closest_location_label = ctk.CTkLabel(self, 
                                                   text="",
                                                   fg_color="#26092F",
                                                   font=("Cascadia Code Light", 20))
        self.closest_location_label.place(x=464, y=375)

        self.open_link_button = ctk.CTkButton(self, 
                                              text="Watch live", 
                                              state="disabled",
                                              fg_color="#BF3EF0",
                                              hover_color="#7F3EF0",
                                              width=100,  
                                              height=40,
                                              font=("Verdana", 19))
        self.open_link_button.place(x=553, y=427)

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
            link1_button.pack(pady=4)

            link2_button = ctk.CTkButton(popup, text="IP API", 
                                         command=lambda: webbrowser.open("https://ipinfo.io/"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link2_button.pack(pady=4)

            link3_button = ctk.CTkButton(popup, text="CustomTkinter", 
                                         command=lambda: webbrowser.open("https://github.com/TomSchimansky/CustomTkinter"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link3_button.pack(pady=4)

            link3_button = ctk.CTkButton(popup, text="Pywebview", 
                                         command=lambda: webbrowser.open("https://pywebview.flowrl.com/"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link3_button.pack(pady=4)

        def show_how_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x300")
            popup.title("How does it work")
            popup.resizable(False, False)
            popup.grab_set()

            with open("AURORIS/how_does_it_work.txt") as file:
                text = file.read()

            scrollable_frame = ctk.CTkScrollableFrame(popup)
            scrollable_frame.pack(fill="both", expand=True)

            label = ctk.CTkLabel(scrollable_frame, text=text, 
                                 font=("Verdana", 13))
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
                                         command=lambda: self.open_live_in_window("https://explore.org/livecams/UAF/aurora-cam"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link1_button.pack(pady=4)

            link2_button = ctk.CTkButton(popup, text="Vorkuta, Russia",
                                          command=lambda: self.open_live_in_window("https://starvisor.net/vrkt/"),
                                          fg_color="#BF3EF0",
                                          hover_color="#7F3EF0")
            link2_button.pack(pady=4)

            link3_button = ctk.CTkButton(popup, text="Rotstund, Norway", 
                                         command=lambda: self.open_live_in_window("https://lyngen-north.com/aurora-borealis-live-cam"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link3_button.pack(pady=4)

            link4_button = ctk.CTkButton(popup, text="Abisko, Sweden", 
                                         command=lambda: self.open_live_in_window("https://lightsoverlapland.com/aurora-webcam/"),
                                         fg_color="#BF3EF0",
                                         hover_color="#7F3EF0")
            link4_button.pack(pady=4)

        self.resources_button = ctk.CTkButton(self, text="Resources", 
                                              command=show_resources_popup, 
                                              width=70,  
                                              height=30,  
                                              fg_color="#26092F",
                                              hover_color="#6FF1FF",
                                              font=("Verdana", 14), 
                                              text_color="#C2BBC5")
        self.resources_button.place(x=60, y=9)

        self.how_button = ctk.CTkButton(self, text="How does it work", 
                                         command=show_how_popup, 
                                         width=70,  
                                         height=30,  
                                         fg_color="#26092F",
                                         hover_color="#6FF1FF",
                                         font=("Verdana", 14), 
                                         text_color="#C2BBC5")
        self.how_button.place(x=160, y=10)

        self.live_button = ctk.CTkButton(self, text="Live transmissions", 
                                          command=show_live_popup, 
                                          width=70,  
                                          height=30,  
                                          fg_color="#26092F",
                                          hover_color="#6FF1FF",
                                          font=("Verdana", 14), 
                                          text_color="#C2BBC5")
        self.live_button.place(x=310, y=10)

        github_image = ctk.CTkImage(Image.open("AURORIS/src/imgs/git.png"), size=(25, 25))
        self.github_button = ctk.CTkButton(self, text="", 
                                           image=github_image,
                                           command=github_open, 
                                           width=25,  
                                           height=25,  
                                           fg_color="#1B1F23",
                                           hover_color="#6FF1FF")
        self.github_button.place(x=10, y=6)

    def on_check_button_click(self):
        lat, long, city = get_user_location()
        
        if lat is None or long is None:
            self.result_label.configure(text="Failed to retrieve location")
        else:
            self.location_label.configure(text=f"{city}\nlat: {lat}\n long: {long}")   
            kp = get_aurora_data(lat, long)
        
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
                distance = haversine(lat, long, location["lat"], location["long"])
                if distance < min_distance:
                    min_distance = distance
                    closest_location = location
            
            self.closest_location_label.configure(text=f"{closest_location['name']} ({min_distance:.2f} km)")
            
            self.open_link_button.configure(state="normal")
            
            def open_live_stream():
                self.open_live_in_window(closest_location['link'])

            self.open_link_button.configure(command=open_live_stream)

        else:
            self.no_aurora.configure(text=f"Aurora is visible in your area. Enjoy!:D")

    #webview 
    def open_live_in_window(self, url):
        webview.create_window("LIVE AURORA", url, 
                              resizable=False,
                              width=800, 
                              height=600)
        webview.start()
