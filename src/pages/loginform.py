import tkinter as tk
from tkinter import ttk, messagebox
from src.pages.home import FirstPage

class LoginPage:
    def __init__(self):
        self.TB_root = tk.Tk()
        self.TB_root.title("Login Form")

        # Increase the size of the overall page
        self.TB_root.geometry("600x500")

        # Center the window on the screen
        self.center_window()

        # Set up the UI components using the grid geometry manager
        self.setup_ui()

    def center_window(self):
        # Calculate the position to center the window
        screen_width = self.TB_root.winfo_screenwidth()
        screen_height = self.TB_root.winfo_screenheight()
        window_width = 600
        window_height = 500

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set the window position
        self.TB_root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def setup_ui(self):
        # Create the main background frame
        self.username_label = tk.Label(text="Username:", font=("Arial", 14, "bold"))
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.username_entry = tk.Entry(self.TB_root, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = tk.Label(text="Email:", font=("Arial", 14, "bold"))
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.email_entry = tk.Entry(self.TB_root, font=("Arial", 14))
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = tk.Label(text="Password:", font=("Arial", 14, "bold"))
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.password_entry = tk.Entry(self.TB_root, show='*', font=("Arial", 14))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.signup_button = ttk.Button(text="Signup", style="Rounded.TButton", command=self.signup)
        self.signup_button.grid(row=3, column=0, columnspan=2, pady=15)

        self.login_button = ttk.Button(text="Login", style="Rounded.TButton", command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=15)
        self.login_button.grid_remove()  # Initially hide the login button

        self.toggle_button_text = tk.StringVar()
        self.toggle_button_text.set("Not a user, Create account")
        self.toggle_button = ttk.Button(textvariable=self.toggle_button_text, command=self.toggle_email_entry)
        self.toggle_button.grid(row=5, column=0, columnspan=2, pady=15)

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not username or not email or not password:
            messagebox.showerror("Error", "Please fill all the required credentials.")
            return

        messagebox.showinfo("Success", "Sign up successful.")
        FirstPage()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username  or not password:
            messagebox.showerror("Error", "Please fill all the required credentials.")
            return

        messagebox.showinfo("Success", "Login successful.")
        FirstPage()

    def toggle_email_entry(self):
        # Toggle visibility of email label and entry
        if self.email_label.winfo_ismapped():
            self.email_label.grid_remove()
            self.email_entry.grid_remove()
            self.login_button.grid()
            self.signup_button.grid_remove()
            self.toggle_button_text.set("Already registered, try signing in")
        else:
            self.email_label.grid()
            self.email_entry.grid()
            self.login_button.grid_remove()
            self.signup_button.grid()
            self.toggle_button_text.set("Not a user, Create account")

    def run(self):
        # Run the Tkinter main loop
        self.TB_root.mainloop()
    