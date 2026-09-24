from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

raam = Tk()
raam.title("Brlrlrlrlrrl")
raam.geometry("1024x768")

s = ttk.Style()
s.theme_use('clam')
#s.configure('Custom.TButton', borderwidth=0, relief='flat')
s.configure('Custom.TButton', borderwidth=0, relief='flat', highlightthickness=0)

txt1 = ttk.Label(raam, text="AAAAAAAAAAAAAAAAAAAAAAA")
txt1.place(x = 350, y = 150)

mass = Image.open("Mass.png").resize((1024,768))
mass = ImageTk.PhotoImage(mass)
mass1 = ttk.Label (image=mass)
mass1.place(x=0, y=0)

album = Image.open("lnf.png").resize((110,110))
album = ImageTk.PhotoImage(album)

skull = Image.open("text.apng").resize((110,110))
skull = ImageTk.PhotoImage(skull)

butt1 = ttk.Button(raam, text="BRLR", style='Custom.TButton')
butt1.place(x = 450, y = 250)



raam.mainloop()
