# user_authentication.py

from tkinter import messagebox
from firebase_connector import db

def save_user_info(username, email, password):
    try:
        doc_ref = db.collection('users').document(username)
        doc_ref.set({
            'username': username,
            'email': email,
            'password': password
        })
        messagebox.showinfo("Success", "Sign up successful.")
        return True

    except Exception as e:
        messagebox.showerror("Error", f"Failed to sign up: {e}")
        return False
