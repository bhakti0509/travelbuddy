from google.cloud import firestore
import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.database.user_repo import save_user_info


class LoginPage:

    def __init__(self):
        # Initialize the Tkinter root window
        self.TB_root = tk.Tk()
        self.TB_screen_width = self.TB_root.winfo_screenwidth()
        self.TB_screen_height = self.TB_root.winfo_screenheight()
        self.TB_root.title("Login Form")
        self.TB_root.geometry(f"{self.TB_screen_width//3}x{self.TB_screen_height//2}")
        self.TB_root.configure(bg="#192f44")

        #Set up the UI components
        self.setup_ui()

    def setup_ui(self):

        #create the main background frame
        self.username_label = tk.Label(text = "Username:").place(x = 100,y=100)
        self.username_entry = tk.Entry(self.TB_root)
        self.username_entry.place(x = 250,y = 100)

        self.email_label = tk.Label(text = "Email:").place(x = 100,y=150)
        self.email_entry = tk.Entry(self.TB_root)
        self.email_entry.place(x=250, y = 150)

        self.password_label = tk.Label(text = "Password:").place(x = 100,y=200)
        self.password_entry = tk.Entry(self.TB_root,show='*')
        self.password_entry.place(x = 250,y = 200)


        #create sign-up button
        self.sign_up_button = ttk.Button(text = "Sign-up",style = "Rounded.TButton",command = self.sign_up)
        self.sign_up_button.pack()
        self.sign_up_button.place(x=250, y=300, anchor='nw')
        
    
        #create login button
        self.login_button = ttk.Button(text = "Login",style = "Rounded.TButton",command = self.login)
        self.login_button.pack()
        self.login_button.place(x=350, y=300, anchor='nw')

        
    def sign_up(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not username or not email or not password:
            messagebox.showerror("Error", "Please fill all the required credentials.")
            return
        
        
        # Save user info to the database
        saved_info = save_user_info(username, email, password)

        if saved_info:
            messagebox.showinfo("Success", "Sign up successful.")
            self.firstPage()

        else:
            messagebox.showinfo("Error","Failed to sign up")
        

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password :
            messagebox.showerror("Error", "Please fill all the required credentials.")
            return

        messagebox.showinfo("Success", "Login successful.")

        self.firstPage()


        # Check if username and password match (not implemented in this example)

        # Authenticate user using Firebase Admin SDK (not implemented in this example)

    def show_destination(self):
        option = self.destination_options.get()
        if option == "By Price":
            messagebox.showinfo("Destination", "You chose destination by Price!")
            

        elif option == "By Vibe":
            messagebox.showinfo("Destination", "You chose destination by Vibe!")
        elif option == "By Location":
            messagebox.showinfo("Destination", "You chose destination by Location!")

    
    def run(self):
        # Run the Tkinter main loop
        self.TB_root.mainloop()
        
app = LoginPage()
app.run()




