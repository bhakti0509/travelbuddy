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
    
def get_user_info(username, password):
    try:
        # Get the user document with matching username 
        user_ref = db.collection('users').document(username)
        user = user_ref.get()
        user_data = user.to_dict()
        
        # Check if the user exists and the password is correct
        if user.exists and user_data['password'] == password:
            return True
        else:
            return False

    except Exception as e:
        print("Error", f"Failed to sign up: {e}")
        return False



