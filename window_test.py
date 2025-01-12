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

        def on_check_button_click():
            print("button pressed")

        def github_open():
            webbrowser.open("https://github.com/werixx1/AURORIS")
        
        def show_resources_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("Resources")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="Wybierz link do zasobów:", font=("Verdana", 14))
            label.pack(pady=10)

            link1_button = ctk.CTkButton(popup, text="Link 1", command=lambda: webbrowser.open("https://www.link1.com"))
            link1_button.pack(pady=5)

            link2_button = ctk.CTkButton(popup, text="Link 2", command=lambda: webbrowser.open("https://www.link2.com"))
            link2_button.pack(pady=5)

            link3_button = ctk.CTkButton(popup, text="Link 3", command=lambda: webbrowser.open("https://www.link3.com"))
            link3_button.pack(pady=5)

        def show_how_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("How does it work")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="To jest tekst wyjaśnienia jak działa aplikacja.", font=("Verdana", 14))
            label.pack(pady=50)

        def show_live_popup():
            popup = ctk.CTkToplevel(self)
            popup.geometry("300x200+500+200")
            popup.title("Live transmissions")
            popup.resizable(False, False)
            popup.grab_set()

            label = ctk.CTkLabel(popup, text="Wybierz link do transmisji na żywo:", font=("Verdana", 14))
            label.pack(pady=10)

            link1_button = ctk.CTkButton(popup, text="Link 1", command=lambda: webbrowser.open("https://www.live1.com"))
            link1_button.pack(pady=5)

            link2_button = ctk.CTkButton(popup, text="Link 2", command=lambda: webbrowser.open("https://www.live2.com"))
            link2_button.pack(pady=5)

            link3_button = ctk.CTkButton(popup, text="Link 3", command=lambda: webbrowser.open("https://www.live3.com"))
            link3_button.pack(pady=5)

        self.start_button = ctk.CTkButton(self, text="start", 
                                          command=on_check_button_click, 
                                          width=170,  
                                          height=55,  
                                          fg_color="#BF3EF0",
                                          hover_color="#7F3EF0",
                                          font=("Verdana", 25))
        self.start_button.grid(row=3, column=0, padx=90, pady=60, sticky="sw")

        self.resources_button = ctk.CTkButton(self, text="Resources", 
                                              command=show_resources_popup, 
                                              width=70,  
                                              height=30,  
                                              fg_color="#1D1C1C",
                                              hover_color="#360C47",
                                              font=("Verdana", 14), 
                                              text_color="#838383")
        self.resources_button.grid(row=0, column=0, padx=90, pady=12, sticky="nw")

        self.how_button = ctk.CTkButton(self, text="How does it work", 
                                         command=show_how_popup, 
                                         width=70,  
                                         height=30,  
                                         fg_color="#1D1C1C",
                                         hover_color="#360C47",
                                         font=("Verdana", 14), 
                                         text_color="#838383")
        self.how_button.grid(row=0, column=0, padx=188, pady=12, sticky="nw")

        self.live_button = ctk.CTkButton(self, text="Live transmissions", 
                                          command=show_live_popup, 
                                          width=70,  
                                          height=30,  
                                          fg_color="#1D1C1C",
                                          hover_color="#360C47",
                                          font=("Verdana", 14), 
                                          text_color="#838383")
        self.live_button.grid(row=0, column=0, padx=338, pady=12, sticky="nw")

        self.github_button = ctk.CTkButton(self, text="Github", 
                                           command=github_open, 
                                           width=50,  
                                           height=30,  
                                           fg_color="#803EA0",
                                           hover_color="#360C47",
                                           font=("Verdana", 14), 
                                           text_color="#E8CFF5")
        self.github_button.grid(row=0, column=1, padx=0, pady=12, sticky="nw")

if __name__ == "__main__":
    app = AuroraApp()
    app.mainloop()
