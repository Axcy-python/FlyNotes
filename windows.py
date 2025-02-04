import customtkinter as ctk
from PIL import Image
from widgets import SmallCardInfo, EntryWidget, FoldersWidget


class WelcomeWin:
    def __init__(self, parent: ctk.CTk) -> None:
        self.__parent: ctk.CTk = parent
        self.__parent.resizable(False, False)
        self.__cards_data: list[dict[str, ctk.CTkImage]] = [
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Your Notes, Smarter Than Ever"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Effortlessly Transcribe Your Voice Into Notes"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Create to-do lists"},
            {"image": ctk.CTkImage(Image.open("static/icons/ai_stars_ico.png"), size=(40, 40)), "text": "Ultimate Note-Taking"}
        ]

        self.__longest_text_width = self.__longest_text()
        self.__is_builded = False


    def build(self) -> None:
        if not self.__is_builded:
            self.__shortkeys()
            self.__is_builded = True

            title_label = ctk.CTkLabel(self.__parent, text="Welcome to Fly Notes", font=ctk.CTkFont(size=38, weight="bold"))
            title_label.pack(pady = (60, 0))

            title_info = ctk.CTkLabel(self.__parent, text="Fly Notes — quick and effortless notes on the go!", font=ctk.CTkFont(size=14))
            title_info.pack(pady = (0, 60))

            for card_data in self.__cards_data:
                card: ctk.CTkFrame = SmallCardInfo(self.__parent)
                card.build(card_data["image"], card_data["text"], width=self.__longest_text_width, height=40)
                card.pack(pady=4)


            continue_button = ctk.CTkButton(self.__parent, text="Continue", width=20, command=self.__continue)
            continue_button.pack(side="bottom", pady=(0, 20))


    def destroy(self) -> None:
        if self.__is_builded:
            self.__is_builded = False
            for widget in self.__parent.winfo_children():
                widget.destroy()
            self.__unbind()


    def __continue(self, *args) -> None:
        self.destroy()
        playground_win = PlaygroundWin(self.__parent)
        playground_win.build()


    def __unbind(self) -> None:
        self.__parent.unbind("<Return>")


    def __longest_text(self) -> int:
        longest_text = max(self.__cards_data, key=lambda x: len(x["text"]))["text"]
        label = ctk.CTkLabel(self.__parent, text=longest_text, text_color=["gray86", "gray17"])
        label.pack()
        label.update_idletasks()
        width = label.winfo_width()
        label.destroy()
        return width


    def __shortkeys(self) -> None:
        self.__parent.bind("<Return>", self.__continue)
    

class PlaygroundWin:
    def __init__(self, parent: ctk.CTk) -> None:
        self.__parent: ctk.CTk = parent
        self.__is_builded = False
        self.__parent.geometry("1080x720")
        self.__parent.resizable(True, True)
        self.__parent.center_window()


    def build(self) -> None:
        if not self.__is_builded:
            self.__is_builded = True
            folder_widget = FoldersWidget(self.__parent, width=190, fg_color="red")
            folder_widget.pack(side="left", fill="y")
            folder_widget.build()


    def __shortkeys(self) -> None:
        pass