import customtkinter as ctk
import webbrowser
from PIL import Image

class AuroraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AURORIS")
        self.geometry("900x600")
        self.resizable(False, False)
        self.bg_image = ctk.CTkImage(Image.open("background.png"), size=(900, 600))
        self.bg_image_label = ctk.CTkLabel(self, text="", image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0, rowspan=5, columnspan=5)

        #to check if buttons are working
        def on_check_button_click():
            print("button pressed")

        def github_open():
            webbrowser.open("https://github.com/werixx1/AURORIS")

        
        self.start_button = ctk.CTkButton(self, text="start", 
                                                command=on_check_button_click, 
                                                width=170,  
                                                height=55,  
                                               #corner_radius=50,
                                                fg_color="#BF3EF0",
                                                hover_color="#7F3EF0",
                                                font=("Verdana", 25))
        self.start_button.grid(row=3, column=0, padx=90, pady=60, sticky="sw")

        self.resources_button = ctk.CTkButton(self, text="Resources", 
                                                command=on_check_button_click, 
                                                width=70,  
                                                height=30,  
                                                fg_color="#1D1C1C",
                                                hover_color="#360C47",
                                                font=("Verdana", 14), 
                                                text_color="#838383"
                                                )                             
        self.resources_button.grid(row=0, column=0, padx=90, pady=12, sticky="nw")

        self.how_button = ctk.CTkButton(self, text="How does it work", 
                                                command=on_check_button_click, 
                                                width=70,  
                                                height=30,  
                                                fg_color="#1D1C1C",
                                                hover_color="#360C47",
                                                font=("Verdana", 14), 
                                                text_color="#838383"
                                                )                             
        self.how_button.grid(row=0, column=0, padx=188, pady=12, sticky="nw")

        self.live_button = ctk.CTkButton(self, text="Live transmissions", 
                                                command=on_check_button_click, 
                                                width=70,  
                                                height=30,  
                                                fg_color="#1D1C1C",
                                                hover_color="#360C47",
                                                font=("Verdana", 14), 
                                                text_color="#838383"
                                                )                             
        self.live_button.grid(row=0, column=0, padx=338, pady=12, sticky="nw")

        self.github_button = ctk.CTkButton(self, text="Github", 
                                                 command=github_open, 
                                                 width=50,  
                                                 height=30,  
                                                 fg_color="#803EA0",
                                                 hover_color="#360C47",
                                                 font=("Verdana", 14), 
                                                 text_color="#E8CFF5"
                                                 )                             
        self.github_button.grid(row=0, column=1, padx=0, pady=12, sticky="nw")

if __name__ == "__main__":
    app = AuroraApp()
    app.mainloop()


