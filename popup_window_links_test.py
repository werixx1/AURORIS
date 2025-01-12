import webbrowser
import customtkinter as ctk

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x300")
        self.resizable(False, False)
        window_width = 400
        window_height = 300


        screen_width = self.winfo_screenwidth()  
        screen_height = self.winfo_screenheight() 
        position_top = int(screen_height / 2 - window_height / 2)  
        position_right = int(screen_width / 2 - window_width / 2) 
        
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        def open_link(url):
            webbrowser.open(url)
        
        def show_link_popup():
            popup_width = 300
            popup_height = 200
            
            screen_width = self.winfo_screenwidth()  # Szerokość ekranu
            screen_height = self.winfo_screenheight()  # Wysokość ekranu
            position_top = int(screen_height / 2 - popup_height / 2)  # Pozycja y
            position_right = int(screen_width / 2 - popup_width / 2)  # Pozycja x
            
            # Tworzenie popup
            self.popup = ctk.CTkToplevel(self)
            self.popup.geometry(f"{popup_width}x{popup_height}+{position_right}+{position_top}")  # Ustawienie pozycji
            self.popup.title("Linki")
            
            # Zablokowanie zmiany rozmiaru okna popup
            self.popup.resizable(False, False)

            # Ustawienie okna popup jako modalne (na wierzchu)
            self.popup.grab_set()  # Blokuje interakcję z głównym oknem

            label = ctk.CTkLabel(self.popup, text="Wybierz link do otwarcia:", font=("Verdana", 14))
            label.pack(pady=10)
            
            # Linki jako przyciski
            link1_button = ctk.CTkButton(self.popup, text="Link 1", command=lambda: open_link("https://www.link1.com"))
            link1_button.pack(pady=5)
            
            link2_button = ctk.CTkButton(self.popup, text="Link 2", command=lambda: open_link("https://www.link2.com"))
            link2_button.pack(pady=5)
            
            link3_button = ctk.CTkButton(self.popup, text="Link 3", command=lambda: open_link("https://www.link3.com"))
            link3_button.pack(pady=5)
        
        # Funkcja do pokazania popup z tekstem po kliknięciu przycisku "Pokaz tekst"
        def show_text_popup():
            # Rozmiar okna popup
            popup_width = 300
            popup_height = 200
            
            # Obliczanie pozycji, aby wyśrodkować popup na ekranie
            screen_width = self.winfo_screenwidth()  # Szerokość ekranu
            screen_height = self.winfo_screenheight()  # Wysokość ekranu
            position_top = int(screen_height / 2 - popup_height / 2)  # Pozycja y
            position_right = int(screen_width / 2 - popup_width / 2)  # Pozycja x
            
            # Tworzenie popup
            self.popup = ctk.CTkToplevel(self)
            self.popup.geometry(f"{popup_width}x{popup_height}+{position_right}+{position_top}")  # Ustawienie pozycji
            self.popup.title("Popup z tekstem")
            
            # Zablokowanie zmiany rozmiaru okna popup
            self.popup.resizable(False, False)

            # Ustawienie okna popup jako modalne (na wierzchu)
            self.popup.grab_set()  # Blokuje interakcję z głównym oknem

            label = ctk.CTkLabel(self.popup, text="To jest tekst w popupie!\n Możesz dodać więcej treści.", font=("Verdana", 10))
            label.pack(pady=40)

        # Przyciski
        self.github_button = ctk.CTkButton(self, text="Github", 
                                            width=100, height=40, 
                                            fg_color="#803EA0",
                                            hover_color="#360C47",
                                            font=("Verdana", 14), 
                                            text_color="#E8CFF5", 
                                            command=show_link_popup)  # Wywołanie funkcji po kliknięciu
        self.github_button.grid(row=0, column=0, padx=10, pady=12, sticky="nw")
        
        # Przycisk do wyświetlenia popup z tekstem
        self.text_button = ctk.CTkButton(self, text="Pokaz tekst", 
                                          width=100, height=40, 
                                          fg_color="#36A1E6",
                                          hover_color="#3591E6",
                                          font=("Verdana", 14), 
                                          text_color="#E8CFF5", 
                                          command=show_text_popup)  # Wywołanie funkcji po kliknięciu
        self.text_button.grid(row=1, column=0, padx=10, pady=12, sticky="nw")

# Uruchomienie aplikacji
app = MyApp()
app.mainloop()

