#GUI
import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.font import BOLD
#py-avataaars
import py_avataaars as pa
#files
import shutil

#Lists
list_style = [pa.AvatarStyle.CIRCLE,]
list_skin_color = [pa.SkinColor.LIGHT,]
list_hair_color = [pa.HairColor.BROWN,]
list_facial_hair_type = [pa.FacialHairType.DEFAULT,]
list_facial_hair_color = [pa.HairColor.BLACK,]
list_top_type = [pa.TopType.SHORT_HAIR_SHORT_FLAT,]
list_hat_color = [pa.Color.BLACK,]
list_mouth_type = [pa.MouthType.SMILE,]
list_eye_type = [pa.EyesType.DEFAULT,]
list_eyebrow_type = [pa.EyebrowType.DEFAULT,]
list_nose_type = [pa.NoseType.DEFAULT,]
list_accessories_type = [pa.AccessoriesType.DEFAULT,]
list_clothe_type = [pa.ClotheType.GRAPHIC_SHIRT,]
list_clothe_color = [pa.Color.HEATHER,]
list_clothe_graphic_type = [pa.ClotheGraphicType.BAT,]
#Default
i_style = 0
i_skin_color = 0
i_hair_color = 0
i_facial_hair_type = 0
i_facial_hair_color = 0
i_top_type = 0
i_hat_color = 0
i_mouth_type = 0
i_eye_type = 0
i_eyebrow_type = 0
i_nose_type = 0
i_accessories_type = 0
i_clothe_type = 0
i_clothe_color = 0
i_clothe_graphic_type = 0
#select
custom_style = list_style[i_style]
custom_skin_color = list_skin_color[i_skin_color]
custom_hair_color = list_hair_color[i_hair_color]
custom_facial_hair_type = list_facial_hair_type[i_facial_hair_type]
custom_facial_hair_color = list_hair_color[i_facial_hair_color]
custom_top_type = list_top_type[i_top_type]
custom_hat_color = list_hat_color[i_hat_color]
custom_mouth_type = list_mouth_type[i_mouth_type]
custom_eye_type = list_eye_type[i_eye_type]
custom_eyebrow_type = list_eyebrow_type[i_eyebrow_type]
custom_nose_type = list_nose_type[i_nose_type]
custom_accessories_type = list_accessories_type[i_accessories_type]
custom_clothe_type = list_clothe_type[i_clothe_type]
custom_clothe_color = list_clothe_color[i_clothe_color]
custom_clothe_graphic_type = list_clothe_graphic_type[i_clothe_graphic_type]

class App(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()

class Methods():
    def Nahled():
        avatar = pa.PyAvataaar(
            style=custom_style,
            skin_color=custom_skin_color,
            hair_color=custom_hair_color,
            facial_hair_type=custom_facial_hair_type,
            facial_hair_color=custom_facial_hair_color,
            top_type=custom_top_type,
            hat_color=custom_hat_color,
            mouth_type=custom_mouth_type,
            eye_type=custom_eye_type,
            eyebrow_type=custom_eyebrow_type,
            nose_type=custom_nose_type,
            accessories_type=custom_accessories_type,
            clothe_type=custom_clothe_type,
            clothe_color=custom_clothe_color,
            clothe_graphic_type=custom_clothe_graphic_type,
            )
        avatar.render_png_file('nahled.png')
    def Next(objekt):
        objekt += 1
        Methods.Nahled()
    def Back(objekt):
        objekt -= 1
        Methods.Nahled()
    def Safe():
        avatar = pa.PyAvataaar(
            style=custom_style,
            skin_color=custom_skin_color,
            hair_color=custom_hair_color,
            facial_hair_type=custom_facial_hair_type,
            facial_hair_color=custom_facial_hair_color,
            top_type=custom_top_type,
            hat_color=custom_hat_color,
            mouth_type=custom_mouth_type,
            eye_type=custom_eye_type,
            eyebrow_type=custom_eyebrow_type,
            nose_type=custom_nose_type,
            accessories_type=custom_accessories_type,
            clothe_type=custom_clothe_type,
            clothe_color=custom_clothe_color,
            clothe_graphic_type=custom_clothe_graphic_type,
            )
        avatar.render_png_file('avatar.png')
        files = [('Portable Network Graphics', '*.png'),]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        shutil.move("avatar.png", file.name)

Methods.Nahled()
mainWin = Tk()
mainWin.geometry("600x650")
mainWin.title("GUI for py-avataaars")

#GUI
frame = Frame(mainWin, borderwidth=2)
frame.pack(expand=1, side=TOP)

DescriptionFR = Frame(frame)
DescriptionFR.pack(side=LEFT)
Description1 = Label(DescriptionFR, text=custom_style, font=("Courier New", 18, BOLD))
Description1.pack(fill=X)

LeftFR = Frame(frame)
LeftFR.pack(side=LEFT)
ToolsButton1_1 = Button(LeftFR, text="00001", font=("Courier New", 11, BOLD), borderwidth=5, pady=10, padx=10, action=Methods.Back(i_style))
ToolsButton1_1.pack(fill=X)

LabelFR = Frame(frame)
LabelFR.pack(side=LEFT)
Label1 = Label(LabelFR, text=custom_style, font=("Courier New", 18, BOLD))
Label1.pack(fill=X)

RightFR = Frame(frame)
RightFR.pack(side=LEFT)
ToolsButton2_1 = Button(RightFR, text="00002", font=("Courier New", 11, BOLD), borderwidth=5, pady=10, padx=10, action=Methods.Next(i_style))
ToolsButton2_1.pack(fill=X)

mainWin.mainloop()