from tkinter import*
# from PIL import ImageTk, Image 
win = Tk()

def check_login():
    correct_email = "hello@mail.co.uk"
    correct_password = "password"

    if email_input.get() == correct_email and passwrd_input.get() == correct_password:
        success_screen()
    else:
        error_label.config(text = "Incorrect credentails, try again", fg = "red")

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