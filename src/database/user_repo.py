from src.database.firebase_connector import db

def save_user_info(username, email, password):
    try:
        doc_ref = db.collection('users').document(username)
        doc_ref.set({
            'username': username,
            'email': email,
            'password': password
        })
        return True

    except Exception as e:
        print("Error", f"Failed to sign up: {e}")
        return False
