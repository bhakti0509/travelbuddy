#Importing required modules

from google.cloud import firestore
import json

import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#Firebase connectivity

credentials_path = '/home/bhakti/Desktop/TravelBuddy/pythontkinterproject-firebase-adminsdk-7yprp-dac553bdea.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)

db = firestore.Client.from_service_account_info(credentials_info)


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
        '''
        try:

            doc_ref = db.collection('users').document(username)
            doc_ref.set({
                'username': username,
                'email': email,
                'password': password
            })
            messagebox.showinfo("Success", "Sign up successful.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to sign up: {e}")
        '''
        self.firstPage()
        '''
        # Add a new document with a generated ID
        doc_ref = db.collection(u'users').document(username)
        doc_ref.set({
            u'username': username,
            u'password': password
        })
        '''

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



        #find a destination:
        destFindBy = tk.Label(self.new_window,text='Find Distination By',bg="#000000",font='TimesNewRoman',fg='white')
        destFindBy.pack(side='top',padx=60,pady=80)
        self.destinations = ['Shaniwar Wada','Sinhgad Fort','Swaminarayan Temple','Panshet Dam','Rajgad Fort','Khadakwasla Dam','FC Road',
                             'Lavasa City','Ramdara Temple','Lonavala']
        Combo = ttk.Combobox(self.new_window, values = self.destinations)
        Combo.set("Choose a Destination")
        Combo.pack(padx = 100, pady = 50)

    
    def run(self):
        # Run the Tkinter main loop
        self.TB_root.mainloop()
        
app = LoginPage()
app.run()




