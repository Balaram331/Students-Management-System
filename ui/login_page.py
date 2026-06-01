import tkinter as tk
from tkinter import messagebox


from services.auth_service import login_user
from ui.dashboard import open_dashboard

#main window
window = tk.Tk()
window.title("Login page")
window.geometry("400x300")


#username
username_label = tk.Label(
    window,
    text = "Username")

username_label.pack(pady = 5)
username_entry = tk.Entry(window)
username_entry.pack(pady = 5)


#password
password_label = tk.Label(
    window,
    text = "Password"
)
password_label.pack(pady = 5)

password_entry = tk.Entry(
    window,
    show = "*"
)
password_entry.pack(pady = 5)



#login function

def login():
    username = username_entry.get()
    password = password_entry.get()

    user = login_user(username, password)

    if user:
        messagebox.showinfo(
            "Login successful",
            f"Welcome {user[1]}!"

        )
        window.destroy()   #close the login window
        
        open_dashboard()

    else:
        messagebox.showerror(
            "Login failed",
            "Invalid username or password"
        )


#login button

login_button = tk.Button(
    window,
    text = "Login",
    command = login
)

login_button.pack(pady = 10)

window.mainloop()