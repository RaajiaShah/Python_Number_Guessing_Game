#Importing the tkinter library
from tkinter import *

#instance of tkinter frame
splash_win= Tk()

#title of the window
splash_win.title("Number Guessing Game - Splash Screen")

#size of the window or frame
splash_win.geometry("700x400")

#Removing border of the splash Window
splash_win.configure(bg='#000000')

splash_win.overrideredirect(True)

#label of the window
splash_label= Label(splash_win, text="Number Guessing Game", bg="#000000",
      fg="#ffd902", font="cambria 24 bold" ,width=39).pack(pady=20)
image = PhotoImage(file = "images\logo.png")
Label(splash_win, image=image).pack(pady=20)


Label(splash_win, text="LOADING . . .", bg="#000000",
      fg="#FFBF00", font="cambria 18 bold").pack()


Label(splash_win, text="PLEASE WAIT . . .", bg="#000000",
      fg="#FFBF00", font="cambria 18 bold").pack(pady=38)

# function
def mainWin():
   splash_win.destroy()
   import main
splash_win.after(5000, mainWin)

mainloop()