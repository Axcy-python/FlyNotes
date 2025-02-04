import customtkinter as ctk
from typing import Literal
from PIL import Image
import platform
from pathlib import Path


class SmallCardInfo(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    
    def build(self, image: ctk.CTkImage, text: str|ctk.StringVar, width: int, height: int) -> None:
        image_label = ctk.CTkLabel(self, image=image, text="")
        image_label.pack(side="left", padx=6, pady=6, fill="both")

        label = ctk.CTkLabel(self, text=text, width=width+20, height=height, anchor="w")
        label.pack(padx=6, pady=6)



class TopBarWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)



class EntryWidget(ctk.CTkEntry):
    """Extended Label widget. For first create object, then call place/pack/grid method"""
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.__shortkeys()

    
    def __shortkeys(self) -> None:
        if platform.system() == "Darwin":
            self.bind("<Command-BackSpace>", self.__erase_text)
        else:
            self.bind("<Control-BackSpace>", self.__erase_text)


    def __erase_text(self, event) -> None:
        self.delete(0, 'end')


class FoldersWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.__parent = parent
        self.__is_builded = False
        self.pack_propagate(False)
        self.__foulder_icon: Path = Path("static/icons/folder_ico.png")
        self.__foulder_icon_img = ctk.CTkImage(Image.open(self.__foulder_icon), size=(20, 16))


    def build(self) -> None:
        if not self.__is_builded:
            self.__is_builded = True
            self.update_idletasks()
            self.create_new_folder("Folder 1")
            self.create_new_folder("Folder 2")
            self.create_new_folder("Folder 3")
            self.create_new_folder("Folder 4")

            add_folder_btn = ctk.CTkButton(self, text="+", command=self.on_add_folder_click, corner_radius=50, width=20, height=20)
            add_folder_btn.pack_propagate(False)
            add_folder_btn.pack(side="bottom", pady=4)

    
    def on_add_folder_click(self, event=None):
        self.create_new_folder("New Folder")


    def create_new_folder(self, name: str) -> None:
        folder_bar = ctk.CTkButton(
            self,
            text=name,
            command=None,
            corner_radius=1,
            width=self.winfo_width(),
            height=20,
            image=self.__foulder_icon_img,
            compound="left",
            fg_color=self.__parent.cget("fg_color"),
            anchor="w"
        )
        folder_bar.pack(side="top", fill="x", pady=4)


    def destroy(self) -> None:
        if self.__is_builded:
            self.__is_builded = False
            for widget in self.__parent.winfo_children():
                widget.destroy()

    def __shortkeys(self) -> None:
        pass


    def __on_click(self, event) -> None:
        print(event)
        print(event.__dict__)


class NotesScrollWidget:
    pass


class NoteWidgetWindow:
    pass


class EditNoteFieldWidget:
    pass