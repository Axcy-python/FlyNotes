import customtkinter as ctk
from windows import WelcomeWin, PlaygroundWin
import ctypes

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fly Notes")
        self.geometry("800x600")
        self.center_window()
        self.current_fullscreen = self.attributes("-fullscreen")
        ctk.set_default_color_theme("themes/lavender.json")

    
    def __shortkeys(self) -> None:
        pass


    def show(self) -> None:
        WelcomeWin(self).show()
        

    def center_window(self) -> None:
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')


    def run(self) -> None:
        self.show()
        self.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()