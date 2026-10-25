from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x800")

def show():
    lbl.config(text=cb.get())
    lbl2.config(text=cbt.get())
    lbl3.config(text=cbb.get())
    

# Dropdown options  
a = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
b = ["x", "y", "z", "ouefhawergoprw"]
c = ["Blowing it smoove off", "Utopia Banished", "Agrippa ma nads"]

# Combobox  
cb = ttk.Combobox(root, values=a)
cb.set("Select a fruit")
cb.pack()
cb.place(x = 200, y = 400)
cbt = ttk.Combobox(root, values=b)
cbt.set("You suffer but why?")
cbt.pack()
cbb = ttk.Combobox(root, values=c)
cbb.set("eauhEFUHEFGUH")
cbb.pack()
cbb.place(x = 1, y = 350)

# Button to display selection  
xyz = ttk.Button(root, text="Show Selection", command=show)#.pack()
xyz.place(x = 400, y = 600)


# Label to show selected value  
lbl = Label(root, text=" ")
lbl.pack()
lbl2 = Label(root, text=" ")
lbl2.pack()
lbl3 = Label(root, text=" ")
lbl3.pack()

root.mainloop()