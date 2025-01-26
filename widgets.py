import customtkinter as ctk
from typing import Literal
from PIL import Image


class SmallCardInfo(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    
    def show(self, image: ctk.CTkImage, text: str|ctk.StringVar, width: int, height: int) -> None:
        image_label = ctk.CTkLabel(self, image=image, text="")
        image_label.pack(side="left", padx=6, pady=6, fill="both")

        label = ctk.CTkLabel(self, text=text, width=width+20, height=height, anchor="w")
        label.pack(padx=6, pady=6)


# class WindowButtonsMacOS:
#     """Base functionality for window buttons like close, minimize, maximize"""
#     def __init__(self, parend: ctk.CTk) -> None:
#         self.__parent: ctk.CTk = parend
#         self.__button_size = 13
#         self.__corner_radius = 50
#         self.__button_spacer = 10
#         self.__top_spacer = 10
#         self.__side_spacer = 20
#         self.__close_button_colors = ("#FF5F57", "#FF453A")
#         self.__minimize_button_colors = ("#FFBD2E", "#FFBF00")
#         self.__maximize_button_colors = ("#28C940", "#32D74B")
#         self.__last_x = 0
        

#     def show(self) -> None:
#         #close button
#         close_button = ctk.CTkButton(
#             self.__parent, text="",
#             width=self.__button_size,
#             height=self.__button_size,
#             corner_radius=self.__corner_radius,
#             fg_color=self.__close_button_colors,
#             command=self.__close,
#             hover_color=("#D54C48", "#D33C2E")
#         )
#         close_button.grid(row=0, column=0, padx=(self.__side_spacer, self.__button_spacer), pady=self.__top_spacer)

#         #minimize button
#         self.__minimize_button = ctk.CTkButton(
#             self.__parent, text="",
#             width=self.__button_size,
#             height=self.__button_size,
#             corner_radius=self.__corner_radius,
#             fg_color=self.__minimize_button_colors,
#             command=self.__minimize,
#             hover_color=("#E69D27", "#E6A400")
#         )
#         self.__minimize_button.grid(row=0, column=1, padx=(0, self.__button_spacer), pady=self.__top_spacer)

#         #maximize button
#         self.__maximize_button = ctk.CTkButton(
#             self.__parent, text="",
#             width=self.__button_size,
#             height=self.__button_size,
#             corner_radius=self.__corner_radius,
#             fg_color=self.__maximize_button_colors,
#             hover_color=("#1F9D32", "#2B9D3D")
#         )
#         self.__maximize_button.grid(row=0, column=2, padx=0, pady=self.__top_spacer)
#         self.__maximize_button.bind("<B1-Motion>", self.__on_drag)
#         self.__maximize_button.bind("<ButtonRelease-1>", self.__on_button_release)

        
#     def __close(self) -> None:
#         self.__parent.destroy()


#     def __minimize(self) -> None:
#         self.__parent.iconify()


#     def __half_maximize(self, x: int) -> None:
#         width: int = self.__parent.winfo_screenwidth()
#         height: int = self.__parent.winfo_screenheight()
#         if x > 50:
#             self.__parent.geometry(f'{width//2}x{height-22}+{width//2}+{0}')
#         elif x < -50:
#             self.__parent.geometry(f'{width//2}x{height-22}+{0}+{0}')
#         else:
#             self.__parent.attributes("-fullscreen", not self.__parent.current_fullscreen)
#             self.__parent.current_fullscreen = not self.__parent.current_fullscreen

#             if self.__parent.current_fullscreen:
#                 self.__minimize_button.configure(state="disabled", fg_color="#A0A0A0")
#             else:
#                 self.__minimize_button.configure(state="normal", fg_color=self.__minimize_button_colors)
        
#         self.__last_x = 0


#     def __on_drag(self, event):
#         self.__last_x = event.x

#     def __on_button_release(self, event):
#        self.__half_maximize(self.__last_x)