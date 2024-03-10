from tkinter import *

home = Toplevel()
home.config(bg="#000000")
home.geometry('500x500')
home.title("Number Guessing Game - Home")
home.resizable(width=False, height=False)


def openEasyLevel():
    import easyLevel


def openNormalLevel():
    import normalLevel


def openHardLevel():
    import hardLevel


f = open('playerData.txt','r')
playerName = 'Welcome ' + f.read()
print(playerName)
f.close()

# WIDGETS

# icon image
icon = PhotoImage(file = "images/icon.png")
home.iconphoto(False, icon)

# heading 
Label(home, text="Number Guessing Game", bg="#ffd902",
      fg="#FFFBF5", font="cambria 24 bold", width=29).pack()

# logo image
my_img = PhotoImage(file = "images/logo.png") 
l2 = Label(home,  image=my_img)
l2.pack(pady=12)


Label(home, text=playerName, bg="#000000",
      fg="#FFBF00", font="cambria 18 bold").pack(pady=20)

Label(home, text="Select Your Level", bg="#000000",
      fg="#FFBF00", font="cambria 19 bold").pack()

Button(home, text="Easy Level", command=openEasyLevel, bg="#FFBF00", fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5",
       font="calibri 15 bold", height=2).place(relx = 0.2, rely = 0.8, anchor = CENTER)

Button(home, text="Normal Level", command=openNormalLevel, bg="#FFBF00",
       fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5", font="calibri 15 bold", height=2).place(relx = 0.5, rely = 0.8, anchor = CENTER)

Button(home, text="Hard Level", command=openHardLevel, bg="#FFBF00", fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5",
       font="calibri 15 bold", height=2).place(relx = 0.8, rely = 0.8, anchor= CENTER)

home.mainloop()
