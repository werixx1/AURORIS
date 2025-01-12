import customtkinter as ctk
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

if __name__ == "__main__":
    app = AuroraApp()
    app.mainloop()
