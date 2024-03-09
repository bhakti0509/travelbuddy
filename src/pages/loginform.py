#Importing required modules

from google.cloud import firestore
import json

import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.database.firebase_connector import db
from src.database.user_authenticator import save_user_info


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
        
        messagebox.showinfo("Success", "Sign up successful.")
        
        # Save user info to the database
        save_user_info(username, email, password)
        self.firstPage()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        if not username or not email or not password :
            messagebox.showerror("Error", "Please fill all the required credentials.")
            return

        messagebox.showinfo("Success", "Login successful.")

        self.firstPage()


        # Check if username and password match (not implemented in this example)

        # Authenticate user using Firebase Admin SDK (not implemented in this example)


    def firstPage(self):
        self.TB_root.destroy() 

        self.new_window = tk.Tk()
        self.new_window.title("Travel Buddy")
        self.new_window.geometry(f"{self.TB_screen_width}x{self.TB_screen_height}")
        self.new_window.configure(bg="#00FFFF")
        label = tk.Label(self.new_window, text="YOUR TRAVEL BUDDY FOR EVERYTHING, EVERYWHERE!", font=("TimesNewRoman", 30), bg="#00FFFF", fg="black")
        label.pack(side="top", pady=40)

        self.TB_left_frame = tk.Frame(self.new_window, bg="#00072D",width=self.TB_screen_width // 6.3, height=self.TB_screen_height)
        self.TB_left_frame.pack(side=tk.LEFT)
    
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory, "../assets/TBLogoFinal.png")
        img = ImageTk.PhotoImage(Image.open(img_path))
        self.logo = tk.Label(self.new_window, image=img, background="#00072D")
        self.logo.image = img
        self.logo.pack()
        self.logo.place(x=0, y=0, anchor="nw")

        img2_path = os.path.join(script_directory,"../assets/pune-darshan.jpg")
        img2 = ImageTk.PhotoImage(Image.open(img2_path))
        self.img2place = tk.Label(self.new_window,image= img2)
        self.img2place.image = img2
        self.img2place.pack()
        self.img2place.place(x=1005,y=500, anchor= 'nw')

        img3_path = os.path.join(script_directory,"../assets/img3Final.jpg")
        img3 = ImageTk.PhotoImage(Image.open(img3_path))
        self.img3place = tk.Label(self.new_window,image= img3)
        self.img3place.image = img3
        self.img3place.pack()
        self.img3place.place(x=303.5,y=500, anchor= 'nw')

        self.choose_destination_label = tk.Label(self.new_window, text="Choose a destination:",height=3,width=20,fg='Black',bg='Yellow')
        self.choose_destination_label.config(font=('TimesNewRoman',25))
        self.choose_destination_label.pack(padx=20,pady=20)

        self.destination_options = ttk.Combobox(self.new_window, values=["By Price", "By Vibe", "By Location"],height=30,width=30)
        self.destination_options.config(font=('TimesNewRoman',15))
        self.destination_options.pack(padx=15,pady=15)

        self.choose_button = ttk.Button(self.new_window, text="Choose", command=self.show_destination)
        self.choose_button.pack()


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




