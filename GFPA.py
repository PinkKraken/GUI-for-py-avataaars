#GUI
import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.font import BOLD
#py-avataaars
import py_avataaars as pa
#tools
import shutil

class App(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()

#Lists
list_style = [pa.AvatarStyle.CIRCLE, pa.AvatarStyle.TRANSPARENT]
list_skin_color = [pa.SkinColor.PALE, pa.SkinColor.LIGHT, pa.SkinColor.YELLOW, pa.SkinColor.TANNED, pa.SkinColor.BROWN, pa.SkinColor.DARK_BROWN, pa.SkinColor.BLACK]
list_hair_color = [pa.HairColor.BLACK, pa.HairColor.BROWN_DARK, pa.HairColor.BROWN, pa.HairColor.AUBURN, pa.HairColor.BLONDE, pa.HairColor.BLONDE_GOLDEN, pa.HairColor.RED, pa.HairColor.PASTEL_PINK, pa.HairColor.PLATINUM, pa.HairColor.SILVER_GRAY]
list_facial_hair_type = [pa.FacialHairType.DEFAULT, pa.FacialHairType.MOUSTACHE_FANCY, pa.FacialHairType.MOUSTACHE_MAGNUM, pa.FacialHairType.BEARD_LIGHT, pa.FacialHairType.BEARD_MEDIUM, pa.FacialHairType.BEARD_MAJESTIC]
list_facial_hair_color = [pa.HairColor.BLACK, pa.HairColor.BROWN_DARK, pa.HairColor.BROWN, pa.HairColor.AUBURN, pa.HairColor.BLONDE, pa.HairColor.BLONDE_GOLDEN, pa.HairColor.RED, pa.HairColor.PASTEL_PINK, pa.HairColor.PLATINUM, pa.HairColor.SILVER_GRAY]
list_top_type = [pa.TopType.SHORT_HAIR_SHORT_FLAT, pa.TopType.NO_HAIR, pa.TopType.EYE_PATCH, pa.TopType.HAT, pa.TopType.HIJAB, pa.TopType.TURBAN, pa.TopType.WINTER_HAT1, pa.TopType.WINTER_HAT2, pa.TopType.WINTER_HAT3, pa.TopType.WINTER_HAT4, pa.TopType.SHORT_HAIR_DREADS_01, pa.TopType.SHORT_HAIR_DREADS_02, pa.TopType.SHORT_HAIR_FRIZZLE, pa.TopType.SHORT_HAIR_SHAGGY_MULLET, pa.TopType.SHORT_HAIR_SHORT_CURLY, pa.TopType.SHORT_HAIR_SHORT_ROUND, pa.TopType.SHORT_HAIR_SHORT_WAVED, pa.TopType.SHORT_HAIR_SIDES, pa.TopType.SHORT_HAIR_THE_CAESAR, pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART, pa.TopType.LONG_HAIR_BIG_HAIR, pa.TopType.LONG_HAIR_BOB, pa.TopType.LONG_HAIR_BUN, pa.TopType.LONG_HAIR_CURLY, pa.TopType.LONG_HAIR_CURVY, pa.TopType.LONG_HAIR_DREADS, pa.TopType.LONG_HAIR_FRIDA, pa.TopType.LONG_HAIR_FRO, pa.TopType.LONG_HAIR_FRO_BAND, pa.TopType.LONG_HAIR_NOT_TOO_LONG, pa.TopType.LONG_HAIR_MIA_WALLACE, pa.TopType.LONG_HAIR_SHAVED_SIDES, pa.TopType.LONG_HAIR_STRAIGHT, pa.TopType.LONG_HAIR_STRAIGHT2, pa.TopType.LONG_HAIR_STRAIGHT_STRAND]
list_hat_color = [pa.Color.BLACK, pa.Color.BLUE_01, pa.Color.BLUE_02, pa.Color.BLUE_03, pa.Color.GRAY_01, pa.Color.GRAY_02, pa.Color.HEATHER, pa.Color.RED, pa.Color.PINK, pa.Color.WHITE, pa.Color.PASTEL_BLUE, pa.Color.PASTEL_GREEN, pa.Color.PASTEL_YELLOW, pa.Color.PASTEL_ORANGE, pa.Color.PASTEL_RED]
list_mouth_type = [pa.MouthType.SMILE, pa.MouthType.DEFAULT, pa.MouthType.CONCERNED, pa.MouthType.DISBELIEF, pa.MouthType.EATING, pa.MouthType.GRIMACE, pa.MouthType.SAD, pa.MouthType.SCREAM_OPEN, pa.MouthType.SERIOUS, pa.MouthType.TWINKLE, pa.MouthType.TONGUE, pa.MouthType.VOMIT]
list_eye_type = [pa.EyesType.DEFAULT, pa.EyesType.CLOSE, pa.EyesType.CRY, pa.EyesType.DIZZY, pa.EyesType.EYE_ROLL, pa.EyesType.HAPPY, pa.EyesType.HEARTS, pa.EyesType.SIDE, pa.EyesType.SQUINT, pa.EyesType.SURPRISED, pa.EyesType.WINK, pa.EyesType.WINK_WACKY]
list_eyebrow_type = [pa.EyebrowType.DEFAULT, pa.EyebrowType.DEFAULT_NATURAL, pa.EyebrowType.ANGRY, pa.EyebrowType.ANGRY_NATURAL, pa.EyebrowType.FLAT_NATURAL, pa.EyebrowType.RAISED_EXCITED, pa.EyebrowType.RAISED_EXCITED_NATURAL, pa.EyebrowType.SAD_CONCERNED, pa.EyebrowType.SAD_CONCERNED_NATURAL, pa.EyebrowType.UNI_BROW_NATURAL, pa.EyebrowType.UP_DOWN, pa.EyebrowType.UP_DOWN_NATURAL, pa.EyebrowType.FROWN_NATURAL]
list_nose_type = [pa.NoseType.DEFAULT,]
list_accessories_type = [pa.AccessoriesType.DEFAULT, pa.AccessoriesType.KURT, pa.AccessoriesType.PRESCRIPTION_01, pa.AccessoriesType.PRESCRIPTION_02, pa.AccessoriesType.ROUND, pa.AccessoriesType.SUNGLASSES, pa.AccessoriesType.WAYFARERS]
list_clothe_type = [pa.ClotheType.GRAPHIC_SHIRT, pa.ClotheType.SHIRT_CREW_NECK, pa.ClotheType.SHIRT_SCOOP_NECK, pa.ClotheType.SHIRT_V_NECK, pa.ClotheType.BLAZER_SHIRT, pa.ClotheType.BLAZER_SWEATER, pa.ClotheType.COLLAR_SWEATER, pa.ClotheType.HOODIE, pa.ClotheType.OVERALL]
list_clothe_color = [pa.Color.BLACK, pa.Color.BLUE_01, pa.Color.BLUE_02, pa.Color.BLUE_03, pa.Color.GRAY_01, pa.Color.GRAY_02, pa.Color.HEATHER, pa.Color.RED, pa.Color.PINK, pa.Color.WHITE, pa.Color.PASTEL_BLUE, pa.Color.PASTEL_GREEN, pa.Color.PASTEL_YELLOW, pa.Color.PASTEL_ORANGE, pa.Color.PASTEL_RED]
list_clothe_graphic_type = [pa.ClotheGraphicType.BAT, pa.ClotheGraphicType.CUMBIA, pa.ClotheGraphicType.DEER, pa.ClotheGraphicType.DIAMOND, pa.ClotheGraphicType.HOLA, pa.ClotheGraphicType.PIZZA, pa.ClotheGraphicType.RESIST, pa.ClotheGraphicType.SELENA, pa.ClotheGraphicType.BEAR, pa.ClotheGraphicType.SKULL_OUTLINE, pa.ClotheGraphicType.SKULL]
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

#Some names of Top_type are too long for me :-)
TopType = {
    "Short_Hair_Short_Flat": "Short_Flat",
    "No_Hair": "No_Hair",
    "Eye_Patch": "Eye_Patch",
    "Hat": "Hat",
    "Hijab": "Hijab",
    "Turban": "Turban",
    "Winter_Hat1": "Winter_Hat1",
    "Winter_Hat2": "Winter_Hat2",
    "Winter_Hat3": "Winter_Hat3",
    "Winter_Hat4": "Winter_Hat4",
    "Short_Hair_Dreads_01": "Short_Dreads_01",
    "Short_Hair_Dreads_02": "Short_Dreads_02",
    "Short_Hair_Frizzle": "Short_Frizzle",
    "Short_Hair_Shaggy_Mullet": "Shaggy_Mullet",
    "Short_Hair_Short_Curly": "Short_Curly",
    "Short_Hair_Short_Round": "Short_Round",
    "Short_Hair_Short_Waved": "Short_Waved",
    "Short_Hair_Sides": "Short_Hair_Sides",
    "Short_Hair_The_Caesar": "The_Caesar",
    "Short_Hair_The_Caesar_Side_Part": "The_Caesar2",
    "Long_Hair_Big_Hair": "Long_Big_Hair",
    "Long_Hair_Bob": "Bob",
    "Long_Hair_Bun": "Bun",
    "Long_Hair_Curly": "Long_Curly",
    "Long_Hair_Curvy": "Long_Curvy",
    "Long_Hair_Dreads": "Long_Dreads",
    "Long_Hair_Frida": "Frida",
    "Long_Hair_Fro": "Fro",
    "Long_Hair_Fro_Band": "Fro_Band",
    "Long_Hair_Not_Too_Long": "Not_Too_Long",
    "Long_Hair_Mia_Wallace": "Mia_Wallace",
    "Long_Hair_Shaved_Sides": "Shaved_Sides",
    "Long_Hair_Straight": "Long_Straight",
    "Long_Hair_Straight2": "Long_Straight2",
    "Long_Hair_Straight_Strand": "Straight_Strand"
}

#Some names of Eyebrow_type are too long for me :-)
#

class Methods():
    def Select():
        global custom_style, custom_skin_color, custom_hair_color, custom_facial_hair_type, custom_facial_hair_color, custom_top_type, custom_hat_color, custom_mouth_type, custom_eye_type, custom_eyebrow_type, custom_nose_type, custom_accessories_type, custom_clothe_type, custom_clothe_color, custom_clothe_graphic_type
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
    
    def Preview():
        global Preview
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
        avatar.render_png_file('preview.png')
        img = PhotoImage(file='preview.png')
        Preview.config(image=img)
        Preview.image = img
        
    def Save():
        files = [('Portable Network Graphics', '*.png'),]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        shutil.move("preview.png", file.name)

    #interface
    #-Style
    def Style(move):
        global i_style
        if move == "back":
            if i_style > 0:
                i_style -= 1
            else:
                i_style = 1
        elif move == "next":
            if i_style < 1:
                i_style += 1
            else:
                i_style = 0
        Methods.Select()
        Label1.config(text = custom_style)
        Methods.Preview()
    
    #-Skin color
    def Skin_color(move):
        global i_skin_color
        if move == "back":
            if i_skin_color > 0:
                i_skin_color -= 1
            else:
                i_skin_color = 6
        elif move == "next":
            if i_skin_color < 6:
                i_skin_color += 1
            else:
                i_skin_color = 0
        Methods.Select()
        Label2.config(text = custom_skin_color)
        Methods.Preview()
    
    #-Hair color
    def Hair_color(move):
        global i_hair_color
        if move == "back":
            if i_hair_color > 0:
                i_hair_color -= 1
            else:
                i_hair_color = 9
        elif move == "next":
            if i_hair_color < 9:
                i_hair_color += 1
            else:
                i_hair_color = 0
        Methods.Select()
        Label3.config(text = custom_hair_color)
        Methods.Preview()
    
    #-Facial hair type
    def Facial_hair_type(move):
        global i_facial_hair_type
        if move == "back":
            if i_facial_hair_type > 0:
                i_facial_hair_type -= 1
            else:
                i_facial_hair_type = 5
        elif move == "next":
            if i_facial_hair_type < 5:
                i_facial_hair_type += 1
            else:
                i_facial_hair_type = 0
        Methods.Select()
        Label4.config(text = custom_facial_hair_type)
        Methods.Preview()

    #-Facial hair color
    def Facial_hair_color(move):
        global i_facial_hair_color
        if move == "back":
            if i_facial_hair_color > 0:
                i_facial_hair_color -= 1
            else:
                i_facial_hair_color = 9
        elif move == "next":
            if i_facial_hair_color < 9:
                i_facial_hair_color += 1
            else:
                i_facial_hair_color = 0
        Methods.Select()
        Label5.config(text = custom_facial_hair_color)
        Methods.Preview()

    #-Top type
    def Top_type(move):
        global i_top_type
        if move == "back":
            if i_top_type > 0:
                i_top_type -= 1
            else:
                i_top_type = 34
        elif move == "next":
            if i_top_type < 34:
                i_top_type += 1
            else:
                i_top_type = 0
        Methods.Select()
        Label6.config(text = TopType[str(custom_top_type)])
        Methods.Preview()

    #-Hat color
    def Hat_color(move):
        global i_hat_color
        if move == "back":
            if i_hat_color > 0:
                i_hat_color -= 1
            else:
                i_hat_color = 14
        elif move == "next":
            if i_hat_color < 14:
                i_hat_color += 1
            else:
                i_hat_color = 0
        Methods.Select()
        Label7.config(text = custom_hat_color)
        Methods.Preview()

    #-Mouth type
    def Mouth_type(move):
        global i_mouth_type
        if move == "back":
            if i_mouth_type > 0:
                i_mouth_type -= 1
            else:
                i_mouth_type = 11
        elif move == "next":
            if i_mouth_type < 11:
                i_mouth_type += 1
            else:
                i_mouth_type = 0
        Methods.Select()
        Label8.config(text = custom_mouth_type)
        Methods.Preview()

    #-Eye type
    def Eye_type(move):
        global i_eye_type
        if move == "back":
            if i_eye_type > 0:
                i_eye_type -= 1
            else:
                i_eye_type = 11
        elif move == "next":
            if i_eye_type < 11:
                i_eye_type += 1
            else:
                i_eye_type = 0
        Methods.Select()
        Label9.config(text = custom_eye_type)
        Methods.Preview()
    
    #-Eyebrow type
    def Eyebrow_type(move):
        global i_eyebrow_type
        if move == "back":
            if i_eyebrow_type > 0:
                i_eyebrow_type -= 1
            else:
                i_eyebrow_type = 12
        elif move == "next":
            if i_eyebrow_type < 12:
                i_eyebrow_type += 1
            else:
                i_eyebrow_type = 0
        Methods.Select()
        Label10.config(text = custom_eyebrow_type)
        Methods.Preview()

    #-Nose type
    #-Accessories type
    #-Clothe type
    #-Clothe color
    #-Clothe graphic type

mainWin = Tk()
mainWin.geometry("900x600")
mainWin.title("GUI for py-avataaars (1.0.0)")

frame = Frame(mainWin, borderwidth=2)
frame.pack(expand=1, side=TOP)

#prewiev
PreviewFR = Frame(frame)
PreviewFR.pack(side=LEFT, fill=BOTH)
Preview = Label(PreviewFR, height=320, width=320)
Methods.Select()
Methods.Preview()
Preview.pack(side=TOP)
SaveBTN = Button(PreviewFR, text="Save avatar", font=("Courier New", 18, BOLD), borderwidth=5, pady=5, padx=5, command=lambda:Methods.Save())
SaveBTN.pack(side=TOP)

#interface
InterfaceFR = Frame(frame)
InterfaceFR.pack(side=RIGHT)
#-Style
StyleFR = Frame(InterfaceFR)
StyleFR.pack(side=TOP)

DescriptionFR1 = Frame(StyleFR)
DescriptionFR1.pack(side=LEFT)
Description1 = Label(DescriptionFR1, text="Avatar style:", font=("Courier New", 12, BOLD), width=20)
Description1.pack(fill=X)

LeftFR1 = Frame(StyleFR)
LeftFR1.pack(side=LEFT)
ToolsButton1_1 = Button(LeftFR1, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Style(a))
ToolsButton1_1.pack(fill=X)

LabelFR1 = Frame(StyleFR)
LabelFR1.pack(side=LEFT)
Label1 = Label(LabelFR1, text=custom_style, font=("Courier New", 12, BOLD), width=17)
Label1.pack(fill=X)

RightFR1 = Frame(StyleFR)
RightFR1.pack(side=LEFT)
ToolsButton1_2 = Button(RightFR1, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Style(a))
ToolsButton1_2.pack(fill=X)

#-Skin color
Skin_colorFR = Frame(InterfaceFR)
Skin_colorFR.pack(side=TOP)

DescriptionFR2 = Frame(Skin_colorFR)
DescriptionFR2.pack(side=LEFT)
Description2 = Label(DescriptionFR2, text="Skin color:", font=("Courier New", 12, BOLD), width=20)
Description2.pack(fill=X)

LeftFR2 = Frame(Skin_colorFR)
LeftFR2.pack(side=LEFT)
ToolsButton2_1 = Button(LeftFR2, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Skin_color(a))
ToolsButton2_1.pack(fill=X)

LabelFR2 = Frame(Skin_colorFR)
LabelFR2.pack(side=LEFT)
Label2 = Label(LabelFR2, text=custom_skin_color, font=("Courier New", 12, BOLD), width=17)
Label2.pack(fill=X)

RightFR2 = Frame(Skin_colorFR)
RightFR2.pack(side=LEFT)
ToolsButton2_2 = Button(RightFR2, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Skin_color(a))
ToolsButton2_2.pack(fill=X)

#-Hair color
Hair_colorFR = Frame(InterfaceFR)
Hair_colorFR.pack(side=TOP)

DescriptionFR3 = Frame(Hair_colorFR)
DescriptionFR3.pack(side=LEFT)
Description3 = Label(DescriptionFR3, text="Hair color:", font=("Courier New", 12, BOLD), width=20)
Description3.pack(fill=X)

LeftFR3 = Frame(Hair_colorFR)
LeftFR3.pack(side=LEFT)
ToolsButton3_1 = Button(LeftFR3, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Hair_color(a))
ToolsButton3_1.pack(fill=X)

LabelFR3 = Frame(Hair_colorFR)
LabelFR3.pack(side=LEFT)
Label3 = Label(LabelFR3, text=custom_hair_color, font=("Courier New", 12, BOLD), width=17)
Label3.pack(fill=X)

RightFR3 = Frame(Hair_colorFR)
RightFR3.pack(side=LEFT)
ToolsButton3_2 = Button(RightFR3, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Hair_color(a))
ToolsButton3_2.pack(fill=X)

#-Facial hair type
Facial_hair_typeFR = Frame(InterfaceFR)
Facial_hair_typeFR.pack(side=TOP)

DescriptionFR4 = Frame(Facial_hair_typeFR)
DescriptionFR4.pack(side=LEFT)
Description4 = Label(DescriptionFR4, text="Facial hair type:", font=("Courier New", 12, BOLD), width=20)
Description4.pack(fill=X)

LeftFR4 = Frame(Facial_hair_typeFR)
LeftFR4.pack(side=LEFT)
ToolsButton4_1 = Button(LeftFR4, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Facial_hair_type(a))
ToolsButton4_1.pack(fill=X)

LabelFR4 = Frame(Facial_hair_typeFR)
LabelFR4.pack(side=LEFT)
Label4 = Label(LabelFR4, text=custom_facial_hair_type, font=("Courier New", 12, BOLD), width=17)
Label4.pack(fill=X)

RightFR4 = Frame(Facial_hair_typeFR)
RightFR4.pack(side=LEFT)
ToolsButton4_2 = Button(RightFR4, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Facial_hair_type(a))
ToolsButton4_2.pack(fill=X)

#-Facial hair color
Facial_hair_colorFR = Frame(InterfaceFR)
Facial_hair_colorFR.pack(side=TOP)

DescriptionFR5 = Frame(Facial_hair_colorFR)
DescriptionFR5.pack(side=LEFT)
Description5 = Label(DescriptionFR5, text="Facial hair color:", font=("Courier New", 12, BOLD), width=20)
Description5.pack(fill=X)

LeftFR5 = Frame(Facial_hair_colorFR)
LeftFR5.pack(side=LEFT)
ToolsButton5_1 = Button(LeftFR5, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Facial_hair_color(a))
ToolsButton5_1.pack(fill=X)

LabelFR5 = Frame(Facial_hair_colorFR)
LabelFR5.pack(side=LEFT)
Label5 = Label(LabelFR5, text=custom_facial_hair_color, font=("Courier New", 12, BOLD), width=17)
Label5.pack(fill=X)

RightFR5 = Frame(Facial_hair_colorFR)
RightFR5.pack(side=LEFT)
ToolsButton5_2 = Button(RightFR5, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Facial_hair_color(a))
ToolsButton5_2.pack(fill=X)

#-Top type
Top_typeFR = Frame(InterfaceFR)
Top_typeFR.pack(side=TOP)

DescriptionFR6 = Frame(Top_typeFR)
DescriptionFR6.pack(side=LEFT)
Description6 = Label(DescriptionFR6, text="Hat/Hair:", font=("Courier New", 12, BOLD), width=20)
Description6.pack(fill=X)

LeftFR6 = Frame(Top_typeFR)
LeftFR6.pack(side=LEFT)
ToolsButton6_1 = Button(LeftFR6, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Top_type(a))
ToolsButton6_1.pack(fill=X)

LabelFR6 = Frame(Top_typeFR)
LabelFR6.pack(side=LEFT)
Label6 = Label(LabelFR6, text=TopType[str(custom_top_type)], font=("Courier New", 12, BOLD), width=17)
Label6.pack(fill=X)

RightFR6 = Frame(Top_typeFR)
RightFR6.pack(side=LEFT)
ToolsButton6_2 = Button(RightFR6, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Top_type(a))
ToolsButton6_2.pack(fill=X)

#-Hat color
Hat_colorFR = Frame(InterfaceFR)
Hat_colorFR.pack(side=TOP)

DescriptionFR7 = Frame(Hat_colorFR)
DescriptionFR7.pack(side=LEFT)
Description7 = Label(DescriptionFR7, text="Hat color:", font=("Courier New", 12, BOLD), width=20)
Description7.pack(fill=X)

LeftFR7 = Frame(Hat_colorFR)
LeftFR7.pack(side=LEFT)
ToolsButton7_1 = Button(LeftFR7, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Hat_color(a))
ToolsButton7_1.pack(fill=X)

LabelFR7 = Frame(Hat_colorFR)
LabelFR7.pack(side=LEFT)
Label7 = Label(LabelFR7, text=custom_hat_color, font=("Courier New", 12, BOLD), width=17)
Label7.pack(fill=X)

RightFR7 = Frame(Hat_colorFR)
RightFR7.pack(side=LEFT)
ToolsButton7_2 = Button(RightFR7, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Hat_color(a))
ToolsButton7_2.pack(fill=X)

#-Mouth type
Mouth_typeFR = Frame(InterfaceFR)
Mouth_typeFR.pack(side=TOP)

DescriptionFR8 = Frame(Mouth_typeFR)
DescriptionFR8.pack(side=LEFT)
Description8 = Label(DescriptionFR8, text="Mouth type:", font=("Courier New", 12, BOLD), width=20)
Description8.pack(fill=X)

LeftFR8 = Frame(Mouth_typeFR)
LeftFR8.pack(side=LEFT)
ToolsButton8_1 = Button(LeftFR8, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Mouth_type(a))
ToolsButton8_1.pack(fill=X)

LabelFR8 = Frame(Mouth_typeFR)
LabelFR8.pack(side=LEFT)
Label8 = Label(LabelFR8, text=custom_mouth_type, font=("Courier New", 12, BOLD), width=17)
Label8.pack(fill=X)

RightFR8 = Frame(Mouth_typeFR)
RightFR8.pack(side=LEFT)
ToolsButton8_2 = Button(RightFR8, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Mouth_type(a))
ToolsButton8_2.pack(fill=X)

#-Eye type
Eye_typeFR = Frame(InterfaceFR)
Eye_typeFR.pack(side=TOP)

DescriptionFR9 = Frame(Eye_typeFR)
DescriptionFR9.pack(side=LEFT)
Description9 = Label(DescriptionFR9, text="Eye type:", font=("Courier New", 12, BOLD), width=20)
Description9.pack(fill=X)

LeftFR9 = Frame(Eye_typeFR)
LeftFR9.pack(side=LEFT)
ToolsButton9_1 = Button(LeftFR9, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Eye_type(a))
ToolsButton9_1.pack(fill=X)

LabelFR9 = Frame(Eye_typeFR)
LabelFR9.pack(side=LEFT)
Label9 = Label(LabelFR9, text=custom_eye_type, font=("Courier New", 12, BOLD), width=17)
Label9.pack(fill=X)

RightFR9 = Frame(Eye_typeFR)
RightFR9.pack(side=LEFT)
ToolsButton9_2 = Button(RightFR9, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Eye_type(a))
ToolsButton9_2.pack(fill=X)

#-Eyebrow type
Eyebrow_typeFR = Frame(InterfaceFR)
Eyebrow_typeFR.pack(side=TOP)

DescriptionFR10 = Frame(Eyebrow_typeFR)
DescriptionFR10.pack(side=LEFT)
Description10 = Label(DescriptionFR10, text="Eyebrow type:", font=("Courier New", 12, BOLD), width=20)
Description10.pack(fill=X)

LeftFR10 = Frame(Eyebrow_typeFR)
LeftFR10.pack(side=LEFT)
ToolsButton10_1 = Button(LeftFR10, text="Back", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="back":Methods.Eyebrow_type(a))
ToolsButton10_1.pack(fill=X)

LabelFR10 = Frame(Eyebrow_typeFR)
LabelFR10.pack(side=LEFT)
Label10 = Label(LabelFR10, text=custom_eyebrow_type, font=("Courier New", 12, BOLD), width=17)
Label10.pack(fill=X)

RightFR10 = Frame(Eyebrow_typeFR)
RightFR10.pack(side=LEFT)
ToolsButton10_2 = Button(RightFR10, text="Next", font=("Courier New", 11, BOLD), borderwidth=3, pady=1, padx=5, command=lambda a="next":Methods.Eyebrow_type(a))
ToolsButton10_2.pack(fill=X)

#-Nose type
i = 1

#-Accessories type
i = 1

#-Clothe type
i = 1

#-Clothe color
i = 1

#-Clothe graphic type
i = 1

mainWin.mainloop()