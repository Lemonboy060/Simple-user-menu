from tkinter import*
# from PIL import ImageTk, Image 
counter = 0
max_attempts = 3

def check_login():
    global counter
    correct_email = "hello@mail.co.uk"
    correct_password = "password"

    if email_input.get() == correct_email and passwrd_input.get() == correct_password:
        success_screen()
    else:
        counter +=1
        attempts_left = max_attempts - counter

        if counter >= max_attempts:
            error_label.config(text = "Incorrect credentials, out of attempts", fg="red")
            email.config(state="disabled")
            passwrd.config(state="disabled")
            button.config(state="disabled")
        else:  
            error_label.config(text=f"Incorrect credentials, {attempts_left} attempts left", fg="red")

def success_screen():
    new_win = Toplevel(win)
    new_win.title("Success")
    new_win.geometry("300x200")
    new_win.config(bg = "light blue")

    Label(new_win, text = "Correct", font=("arial", 16), bg = "light blue").pack(pady=20)
#Login buttons
win.geometry("400x300") # Set window size
win.configure(bg = "light blue")
win.title("My Tkinter Window") # Optional: Set window title

email = Label(win, text = "Enter email:", font = "arial", bg = "light blue", justify= "left")
email .pack(padx=10,pady=10)
email_input = Entry(win,width = 30)
email_input.pack()

passwrd = Label(win,text = "Password:", font = "arial", bg = "light blue", justify = "left")
passwrd .pack(padx=10,pady=10)
passwrd_input = Entry(win,width = 30, show = "*")
passwrd_input.pack()

button = Button(win, text = "Login", bg = "white", fg = "black",command = check_login)
button.pack(pady=(10,20))

error_label = Label(win, text="", font="arial", bg = "light blue")
error_label.pack()

win.mainloop()

# # # Create and place the label
# label = Label(win, text="Welcome!", fg="black", bg="light blue", font=("Arial", 16))
# label.place(x=150, y=50) # Position at (150, 50)
# # Create and place the buttons
# button1 = Button(win, text="Login", fg="black", bg="white")
# button1.place(x=100, y=150) # Position at (100, 150)
# button2 = Button(win, text="Sign Up!", fg="black", bg="white")
# button2.place(x=250, y=150) # Position at (250, 150)
