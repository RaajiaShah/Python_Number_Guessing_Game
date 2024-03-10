from tkinter import * 
import random

easy = Toplevel()
easy.config(bg="#000000")
easy.geometry('500x600')
easy.title("Number Guessing Game - Easy Level")
easy.resizable(width=False, height=False)

answer = random.randint(0, 100)
attempts = 15

def openHomePage():
    easy.destroy()
    import home



def update_result(text):   
      result.configure(text=text)

def printAttempts(_attempts):
    attempt_string = "Attempt left: " + str(_attempts)
    label_attempt = Label(easy,
                          text=attempt_string,
                          width=20,bg="#FFBF00",fg="#FFFBF5",font=("bold", 14))
    label_attempt.place(relx = 0.5, rely = 0.3,anchor=CENTER) 


printAttempts(15)

def play_game():
     global attempts
     print('attempts', attempts)
     guessed_number = number_form.get()
     guessed_number = int(guessed_number)
     
     if attempts != 0:
        print('the guess', guessed_number)
        print('the random', answer)
        if (guessed_number == answer):
            result = "Awesome!!! You just got it right!"
            attempts = 0
            print(attempts)
        else:
            print('removing one attempt')
            attempts = attempts - 1
            if (guessed_number > answer):
                result = "Your guess number is greater than lucky number"
                print('too high', attempts)
            else:
                result ="Your guess number is less than lucky number"
                print('too low', attempts)
            if (attempts == 0):
                result ="No attempts left, better luck next time"
                print('run out', attempts)
        update_result(result)
        printAttempts(attempts)            

   

# WIDGETS

# icon image
icon = PhotoImage(file = "images/icon.png")
easy.iconphoto(False, icon)

# heading  
Label(easy, text="Number Guessing Game", bg="#ffd902",
      fg="#FFFBF5", font="cambria 24 bold", width=29).pack()

# logo image
my_img = PhotoImage(file = "images/logo2.png") 
l2 = Label(easy,  image=my_img )
l2.pack(pady=10)

# entry
number_form = Entry(easy,font="Arial 20",width=20,bg="#000000",fg="#FFFBF5",insertbackground='white')

# buttons
guessed_btn = Button(easy,text="Guess",font="cambria 16 bold", bg="#FFBF00",
        fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5", command=play_game)
exit_btn = Button(easy,text="Exit",font="cambria 18 bold", bg="#FFBF00",
       fg="#FFFBF5", activebackground="#D4A007", activeforeground="#FFFBF5", width=20 ,command=openHomePage)

# guess result
result = Label(easy, text="Guess a number between 0 and 100", bg="#FFBF00",fg="#FFFBF5",
                     font="cambria 14 bold") 

# place
number_form.place(relx = 0.5, rely = 0.5,anchor=CENTER)
guessed_btn.place(relx = 0.7, rely = 0.5,anchor=W) 
exit_btn.place(relx = 0.5, rely = 0.9,anchor=CENTER)
result.place(relx = 0.5, rely = 0.7,anchor=CENTER) 



easy.mainloop()            
