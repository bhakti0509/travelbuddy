import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class HomePage:
    def __init__(self):
        self.home_window = tk.Tk()
        self.home_window.title("Travel Buddy")

        # Increase the size of the overall page
        self.home_window.geometry("600x500")

        # Center the window on the screen
        self.center_window()

        # Set up the UI components using the grid geometry manager
        self.setup_home_page()

    def center_window(self):
        # Calculate the position to center the window
        screen_width = self.home_window.winfo_screenwidth()
        screen_height = self.home_window.winfo_screenheight()
        window_width = 600
        window_height = 500

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set the window position
        self.home_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def setup_home_page(self):
        self.home_window.configure(bg="#00FFFF")
        label = tk.Label(self.home_window, text="YOUR TRAVEL BUDDY FOR EVERYTHING, EVERYWHERE!", font=("TimesNewRoman", 30), bg="#00FFFF", fg="black")
        label.pack(side="top", pady=40)

        self.TB_left_frame = tk.Frame(self.home_window, bg="#00072D", width=self.home_window.winfo_screenwidth() // 6.3, height=self.home_window.winfo_screenheight())
        self.TB_left_frame.pack(side=tk.LEFT)
    
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory, "../../assets/TBLogoFinal.png")
        img = ImageTk.PhotoImage(Image.open(img_path))
        self.logo = tk.Label(self.home_window, image=img, background="#00072D")
        self.logo.image = img
        self.logo.pack()
        self.logo.place(x=0, y=0, anchor="nw")

        img2_path = os.path.join(script_directory,"../../assets/pune-darshan.jpg")
        img2 = ImageTk.PhotoImage(Image.open(img2_path))
        self.img2place = tk.Label(self.home_window,image= img2)
        self.img2place.image = img2
        self.img2place.pack()
        self.img2place.place(x=1005,y=500, anchor= 'nw')

        img3_path = os.path.join(script_directory,"../../assets/img3Final.jpg")
        img3 = ImageTk.PhotoImage(Image.open(img3_path))
        self.img3place = tk.Label(self.home_window,image= img3)
        self.img3place.image = img3
        self.img3place.pack()
        self.img3place.place(x=303.5,y=500, anchor= 'nw')

        self.choose_destination_label = tk.Label(self.home_window, text="Choose a destination:", height=3, width=20, fg='Black', bg='Yellow')
        self.choose_destination_label.config(font=('TimesNewRoman',25))
        self.choose_destination_label.pack(padx=20,pady=20)

        self.destination_options = ttk.Combobox(self.home_window, values=["By Price", "By Vibe", "By Location"],height=30,width=30)
        self.destination_options.config(font=('TimesNewRoman',15))
        self.destination_options.pack(padx=15,pady=15)

        self.choose_button = ttk.Button(self.home_window, text="Choose", command=self.show_destination)
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
        self.home_window.mainloop()
