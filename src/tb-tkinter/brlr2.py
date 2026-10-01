from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys

#def skill_issue
def kill():
    raam.destroy()
    sys.exit()
    
def start():
    skull.place_forget()
    startbutt.place_forget()
    startkill.place_forget()
    skull2.place(x = 275, y = 50, height=210, width=450)
    secondarykill.place(x = 800, y = 70, height=60, width=60)
    workyouasshole()

def workyouasshole():
    it0.place(x = 60, y = 350, height=101, width=105)
    it11.place(x = 60, y = 490, height=101, width=105)
    it12.place(x = 60, y = 640, height=101, width=105)
    ku10.place(x = 260, y = 350, height=101, width=105)
    ku11.place(x = 260, y = 490, height=101, width=105)
    ku12.place(x = 260, y = 640, height=101, width=105)
    lo10.place(x = 460, y = 350, height=101, width=105)
    lo11.place(x = 460, y = 490, height=101, width=105)
    lo12.place(x = 460, y = 640, height=101, width=105)
    me10.place(x = 660, y = 350, height=101, width=105)
    me11.place(x = 660, y = 490, height=101, width=105)
    me12.place(x = 660, y = 640, height=101, width=105)
    th10.place(x = 860, y = 210, height=101, width=105)
    te10.place(x = 860, y = 350, height=101, width=105)
    te11.place(x = 860, y = 490, height=101, width=105)
    te12.place(x = 860, y = 640, height=101, width=105)
    
def valik():
    skull3.place(x = 275, y = 50, height=210, width=450)
    skull2.place_forget()
    it0.place_forget()
    it11.place_forget()
    it12.place_forget()
    ku10.place_forget()
    ku11.place_forget()
    ku12.place_forget()
    lo10.place_forget()
    lo11.place_forget()
    lo12.place_forget()
    me10.place_forget()
    me11.place_forget()
    me12.place_forget()
    th10.place_forget()
    te10.place_forget()
    te11.place_forget()
    te12.place_forget()

#def final():

#Raam
raam = Tk()
raam.title("Brlrlrlrlrrl")
raam.geometry("1024x768")

#No idea, not touching it lol
s = ttk.Style()
s.theme_use('clam')
#s.configure('Custom.TButton', borderwidth=0, relief='flat')
s.configure('Custom.TButton', borderwidth=0, relief='flat', highlightthickness=0)
raam.configure(bg='darkblue')
raam.wm_attributes('-transparentcolor', '#ab23ff')

#PICTURES ON MY MIND
text1 = Image.open("retor.png").resize((450,210))
text1 = ImageTk.PhotoImage(text1)
skull = ttk.Label(image=text1)
skull.place(x = 275, y = 50, height=210, width=450)
text2 = Image.open("enter.png").resize((175,225))
text2 = ImageTk.PhotoImage(text2)
text3 = Image.open("exit.png").resize((175,225))
text3 = ImageTk.PhotoImage(text3)
text4 = Image.open("klass.png").resize((450,210))
text4 = ImageTk.PhotoImage(text4)
skull2 = ttk.Label(image=text4)
text5 = Image.open("valik.png").resize((450,210))
text5 = ImageTk.PhotoImage(text5)
skull3 = ttk.Label(image=text5)
x = Image.open("x.png").resize((50,50))
x = ImageTk.PhotoImage(x)

i0 = Image.open("10it.png").resize((100,100))
i0 = ImageTk.PhotoImage(i0)
i1 = Image.open("11it.png").resize((100,100))
i1 = ImageTk.PhotoImage(i1)
i2 = Image.open("12it.png").resize((100,100))
i2 = ImageTk.PhotoImage(i2)

k0 = Image.open("10ku.png").resize((100,100))
k0 = ImageTk.PhotoImage(k0)
k1 = Image.open("11ku.png").resize((100,100))
k1 = ImageTk.PhotoImage(k1)
k2 = Image.open("12ku.png").resize((100,100))
k2 = ImageTk.PhotoImage(k2)

l0 = Image.open("10lo.png").resize((100,100))
l0 = ImageTk.PhotoImage(l0)
l1 = Image.open("11lo.png").resize((100,100))
l1 = ImageTk.PhotoImage(l1)
l2 = Image.open("12lo.png").resize((100,100))
l2 = ImageTk.PhotoImage(l2)

m0 = Image.open("10me.png").resize((100,100))
m0 = ImageTk.PhotoImage(m0)
m1 = Image.open("11me.png").resize((100,100))
m1 = ImageTk.PhotoImage(m1)
m2 = Image.open("12me.png").resize((100,100))
m2 = ImageTk.PhotoImage(m2)

h0 = Image.open("10th.png").resize((100,100))
h0 = ImageTk.PhotoImage(h0)
t0 = Image.open("10te.png").resize((100,100))
t0 = ImageTk.PhotoImage(t0)
t1 = Image.open("11te.png").resize((100,100))
t1 = ImageTk.PhotoImage(t1)
t2 = Image.open("12te.png").resize((100,100))
t2 = ImageTk.PhotoImage(t2)

#First buttons
startbutt = ttk.Button(raam, text="Sisene", style='Custom.TButton', command = start, image = text2)
startbutt.place(x = 150, y = 350, height=200, width=200) #Viib edasi klasside valiku lehele
startkill = ttk.Button(raam, text=":þ", style='Custom.TButton', command = kill, image = text3)
startkill.place(x = 650, y = 350, height=200, width=200) #Sugleb programmi

#KLASSID BUTTONS
secondarykill = ttk.Button(raam, style='Custom.TButton', command = kill, image = x) #Does as advertised
it0 = ttk.Button(raam, style='Custom.TButton', command = valik, image = i0) #Valib IT tunniplaani (10 - 12)
it11 = ttk.Button(raam, style='Custom.TButton', command = valik, image = i1)
it12 = ttk.Button(raam, style='Custom.TButton', command = valik, image = i2)
ku10 = ttk.Button(raam, style='Custom.TButton', command = valik, image = k0) #Ditto, KU
ku11 = ttk.Button(raam, style='Custom.TButton', command = valik, image = k1)
ku12 = ttk.Button(raam, style='Custom.TButton', command = valik, image = k2)
lo10 = ttk.Button(raam, style='Custom.TButton', command = valik, image = l0) #Ditto, LO
lo11 = ttk.Button(raam, style='Custom.TButton', command = valik, image = l1)
lo12 = ttk.Button(raam, style='Custom.TButton', command = valik, image = l2)
me10 = ttk.Button(raam, style='Custom.TButton', command = valik, image = m0) #Ditto, ME
me11 = ttk.Button(raam, style='Custom.TButton', command = valik, image = m1)
me12 = ttk.Button(raam, style='Custom.TButton', command = valik, image = m2)
th10 = ttk.Button(raam, style='Custom.TButton', command = valik, image = h0) #Ditto, TE/H
te10 = ttk.Button(raam, style='Custom.TButton', command = valik, image = t0)
te11 = ttk.Button(raam, style='Custom.TButton', command = valik, image = t1)
te12 = ttk.Button(raam, style='Custom.TButton', command = valik, image = t2)

#VALIKAINE BUTTONS

#FINAL BUTTONS
FinalKillButton = ttk.Button(raam, text=":þ", style='Custom.TButton', command = kill)
#FinalKillButton.place(x = 450, y = 250, height=100, width=200)


raam.mainloop()
