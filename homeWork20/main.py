from tkinter import *
from tkinter import messagebox
import pickle
import json


def login_pass():
    global login_entry, pass_entry
    with open('login.txt', 'rb') as f:
        data = pickle.load(f)
    if login_entry.get() in data and data[login_entry.get()] == pass_entry.get():
        messagebox.showinfo("Success", "You have successfully logged into your account.")
    else:
        messagebox.showerror("Error", "Login or password is incorrect.")


def register():
    label_error = None
    frame = Frame(root, bd=10)
    frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)

    label = Label(frame, text="Sing Up", font="16")
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text="Sing Up:", font="14")
    label_login.place(relx=0.1, rely=0.25)
    label_pass1 = Label(frame, text="Password:", font="14")
    label_pass1.place(relx=0.05, rely=0.45)
    label_pass2 = Label(frame, text="Password:", font="14")
    label_pass2.place(relx=0.05, rely=0.65)
    login_entry = Entry(frame)
    login_entry.place(relx=0.3, rely=0.25)
    pass1_entry = Entry(frame)
    pass1_entry.place(relx=0.3, rely=0.45)
    pass2_entry = Entry(frame)
    pass2_entry.place(relx=0.3, rely=0.65)


    def singup():
        nonlocal label_error
        error = ""
        if label_error:
            label_error.destroy()

        if len(login_entry.get()) == 0:
            error = "Error login"
        elif len(pass1_entry.get()) < 4:
            error = "Error password"
        elif pass1_entry.get() != pass2_entry.get():
            error = "Error password LENGTH"
        else:
            save()
        label_error = Label(frame, text=error, fg="red")
        label_error.place(rely=0.8)
    def save():
        data = dict()
        data[login_entry.get()] = pass1_entry.get()
        with open('login.txt', 'wb') as f:
            pickle.dump(data, f)
        login()

    button = Button(frame, text="Sing Up", command=singup)
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)


def login():
    global login_entry, pass_entry
    frame = Frame(root, bd=10)
    frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)

    label = Label(frame, text="Sing In", font="16")
    label.place(relwidth=1, relheight=0.1)
    label_login = Label(frame, text="Sing In:", font="14")
    label_login.place(relx=0.1, rely=0.25)
    label_pass1 = Label(frame, text="Password:", font="14")
    label_pass1.place(relx=0.05, rely=0.45)
    login_entry = Entry(frame)
    login_entry.place(relx=0.3, rely=0.25)
    pass_entry = Entry(frame)
    pass_entry.place(relx=0.3, rely=0.45)
    button = Button(frame, text="Sing In", command=login_pass)
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)


HEIGHT = 600
WEIGHT = 600



root = Tk()
root.title("Login and password")
root.geometry(f"{WEIGHT}x{HEIGHT}")
root.resizable(False, False)
root.option_add("*Font", "Calibri")
root.option_add("*Background", "white")
img = PhotoImage(file="images/bg2.gif")
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_singup = Button(root, text="Sing Up", bg="gold", command=register)
button_singup.place(relx=0.2, rely=0.1, relwidth=0.3)
button_singin = Button(root, text="Sing In", bg="gold", command=login)
button_singin.place(relx=0.55, rely=0.1, relwidth=0.3)

root.mainloop()