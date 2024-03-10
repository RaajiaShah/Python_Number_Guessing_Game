from tkinter import *

window = Tk()
window.config(bg="#000000")
window.geometry('500x500')
window.title("Number Guessing Game")
window.resizable(width=False, height=False)


#global variables
player_name = StringVar()
Try = 0

#function
def GameBegin():
      f = open('playerData.txt','w')
      f.write(player_name.get())
      f.close()
      import home


# WIDGETS

# icon image
icon = PhotoImage(file = "images/icon.png")
window.iconphoto(False, icon)

# heading
Label(window, text="Number Guessing Game", bg="#ffd902",
      fg="#F5F5F5", font="cambria 24 bold" ,width=29).pack()

# logo image
my_img = PhotoImage(file = "images/logo.png") 
l2 = Label(window,  image=my_img)
l2.pack(pady=20)

Label(window, text="Enter Your Name", bg="#000000",
      fg="#FFBF00", font="cambria 19 bold").pack(pady=10)

# name entry
name_form = Entry(window, textvariable=player_name, font="Arial 20",width=20,bg="#000000",fg="#FFFBF5",insertbackground='white')
enter = Button(window,text="Enter",font="cambria 16 bold",  bg="#FFBF00",
        fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5", width=15, command=GameBegin)

# place
name_form.place(relx = 0.5, rely = 0.6,anchor=CENTER)
enter.place(relx = 0.5, rely = 0.8, anchor = CENTER)


window.mainloop()