import customtkinter as ctk
from typing import Literal
from PIL import Image
import platform
from pathlib import Path
from database import Folder as FolderModel
from database import db


#  __      __   _                  
#  \ \    / /__| |__ ___ _ __  ___ 
#   \ \/\/ / -_) / _/ _ \ '  \/ -_)
#    \_/\_/\___|_\__\___/_|_|_\___|
                                 
class SmallCardInfo(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    
    def build(self, image: ctk.CTkImage, text: str|ctk.StringVar, width: int, height: int) -> None:
        image_label = ctk.CTkLabel(self, image=image, text="")
        image_label.pack(side="left", padx=6, pady=6, fill="both")

        label = ctk.CTkLabel(self, text=text, width=width+20, height=height, anchor="w")
        label.pack(padx=6, pady=6)


#   _  _     _           __      ___      
#  | \| |___| |_ ___ ___ \ \    / (_)_ _  
#  | .` / _ \  _/ -_|_-<  \ \/\/ /| | ' \ 
#  |_|\_\___/\__\___/__/   \_/\_/ |_|_||_|
#            
class TopBarWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class FoldersWidget(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.__parent = parent
        self.__is_builded = False
        self.pack_propagate(False)
        self.__foulder_icon: Path = Path("static/icons/folder_ico.png")
        self.__foulder_icon_img = ctk.CTkImage(Image.open(self.__foulder_icon), size=(16, 12))
        self.__base_folder_name: str = "Unnamed Folder"


    def build(self) -> None:
        if not self.__is_builded:
            self.__is_builded = True
            self.update_idletasks()
            with db:
                all_folders: FolderModel = FolderModel.select()
                try:
                    for record in all_folders:
                        self.create_folder(name=record.folder_name)
                except:
                    pass
            

            add_folder_btn = ctk.CTkButton(self, text="New folder", command=self.on_add_folder_click, corner_radius=6, anchor="center")
            add_folder_btn.pack_propagate(False)
            add_folder_btn.pack(side="bottom", pady=6, fill="x", padx = 6)

    
    def on_add_folder_click(self, event=None):
        FolderModel(folder_name = self.__base_folder_name).save()
        self.create_folder(self.__base_folder_name)


    def create_folder(self, name: str) -> None:
        folder_bar = ctk.CTkButton(
            self,
            text=name,
            command=None,
            corner_radius=2,
            width=self.winfo_width(),
            height=20,
            image=self.__foulder_icon_img,
            compound="left",
            fg_color=self.cget("fg_color"),
            anchor="w"
        )
        folder_bar.pack(side="top", fill="x", pady=4, ipady=2)


    def destroy(self) -> None:
        if self.__is_builded:
            self.__is_builded = False
            for widget in self.__parent.winfo_children():
                widget.destroy()

    def __shortkeys(self) -> None:
        pass


    def __on_click(self, event) -> None:
        print(event)


class NotesScrollWidget(ctk.CTkScrollableFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.__parent = parent
        self.__is_builded = False


    def build(self) -> None:
        if not self.__is_builded:
            self.__is_builded = True

            for _ in range(30):
                test = ctk.CTkButton(self, height=40, fg_color="red", text="Welcooome")
                test.pack(side="top", fill="x", padx=4, pady=4)
                line = ctk.CTkFrame(self, width=self.cget("width")*0.8, fg_color="#ffffff", height=1, corner_radius=2)
                line.pack(side="top", anchor = "e")
            else:
                line.destroy()
            

class EditNoteFieldWidget:
    pass


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