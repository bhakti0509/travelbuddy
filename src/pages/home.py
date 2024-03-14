from google.cloud import firestore
import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.database.user_repo import save_user_info


class FirstPage:

    def __init__(self):

        #Set up the UI components
        self.setup_ui()

    def setup_ui(self):

        self.firstPage()

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
        img_path = os.path.join(script_directory, "../../assets/TBLogoFinal.png")
        img = ImageTk.PhotoImage(Image.open(img_path))
        self.logo = tk.Label(self.new_window, image=img, background="#00072D")
        self.logo.image = img
        self.logo.pack()
        self.logo.place(x=0, y=0, anchor="nw")

        img2_path = os.path.join(script_directory,"../../assets/pune-darshan.jpg")
        img2 = ImageTk.PhotoImage(Image.open(img2_path))
        self.img2place = tk.Label(self.new_window,image= img2)
        self.img2place.image = img2
        self.img2place.pack()
        self.img2place.place(x=1005,y=500, anchor= 'nw')

        img3_path = os.path.join(script_directory,"../../assets/img3Final.jpg")
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