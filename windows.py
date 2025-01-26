import customtkinter as ctk
from PIL import Image, ImageTk
from widgets import SmallCardInfo


class WelcomeWin:
    def __init__(self, parent: ctk.CTk):
        self.__parent: ctk.CTk = parent
        self.__parent.resizable(False, False)
        self.__cards_data: list[dict[str, ctk.CTkImage]] = [
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Your Notes, Smarter Than Ever"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Effortlessly Transcribe Your Voice Into Notes"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Create to-do lists"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Ultimate Note-Taking"}
        ]

        self.__longest_text_width = self.__longest_text()


    def show(self) -> None:
        title_label = ctk.CTkLabel(self.__parent, text="Welcome to Fly Notes", font=ctk.CTkFont(size=38, weight="bold"))
        title_label.pack(pady = (60, 0))

        title_info = ctk.CTkLabel(self.__parent, text="Fly Notes — quick and effortless notes on the go!", font=ctk.CTkFont(size=14))
        title_info.pack(pady = (0, 60))

        for card_data in self.__cards_data:
            print(self.__longest_text_width)
            card: ctk.CTkFrame = SmallCardInfo(self.__parent)
            card.show(card_data["image"], card_data["text"], width=self.__longest_text_width, height=40)
            card.pack(pady=4)

        
        continue_button = ctk.CTkButton(self.__parent, text="Continue", width=20, command=self.__continue)
        continue_button.pack(side="bottom", pady=(0, 20))


    def __continue(self) -> None:
        print("Continue button pressed")


    def __longest_text(self) -> int:
        longest_text = max(self.__cards_data, key=lambda x: len(x["text"]))["text"]
        label = ctk.CTkLabel(self.__parent, text=longest_text, text_color=["gray86", "gray17"])
        label.pack()
        label.update_idletasks()
        width = label.winfo_width()
        label.destroy()
        return width


    def __shortkeys(self) -> None:
        pass
    

class PlaygroundWin:
    def __init__(self, parent: ctk.CTk) -> None:
        pass


    def show(self) -> None:
        pass


    def __shortkeys(self) -> None:
        pass