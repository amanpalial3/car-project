import mysql.connector
import re

def create_db_connection():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='mysql'
        )
    except Exception as e:
        print("Database connection error:", e)
        return None

def is_valid_email(email):
    # Simple regex for validating an email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def register_user(data):
    username, email, password = data
    # Validation checks
    if not username or not email or not password:
        return "All fields are required."

    if not is_valid_email(email):
        return "Invalid email format."  
    

    mydatabase = create_db_connection()
    if not mydatabase:
        return "Database connection error."

    cursor = mydatabase.cursor()
    
    try:
        cursor.execute("INSERT INTO user_auth (Username, Email, Password) VALUES (%s, %s, %s)", (username, email, password))
        mydatabase.commit()
        return "Registration successful."
    except mysql.connector.IntegrityError:
        return "Username or email already exists."
    except Exception as e:
        print("Registration error:", e)
        return "An error occurred during registration."
    finally:
        cursor.close()
        mydatabase.close()

def get_all_users():
    mydatabase = create_db_connection()
    if not mydatabase:
        return []
    cursor = mydatabase.cursor()
    
    try:
        cursor.execute("SELECT * FROM user_auth")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching users:", e)
        return []
    finally:
        cursor.close()
        mydatabase.close()

def login_user(data):
    mydatabase = create_db_connection()
    if not mydatabase:
        return None
    cursor = mydatabase.cursor()
    
    try:
        cursor.execute("SELECT * FROM user_auth WHERE Email=%s AND Password=%s", data)
        return cursor.fetchone()
    except Exception as e:
        print("Login error:", e)
        return None
    finally:
        cursor.close()
        mydatabase.close()

def delete_user(user_id):
    mydatabase = create_db_connection()
    if not mydatabase:
        return False
    cursor = mydatabase.cursor()
    
    try:
        cursor.execute("DELETE FROM user_auth WHERE id=%s", (user_id,))
        mydatabase.commit()
        return True
    except Exception as e:
        print("Error deleting user:", e)
        return False
    finally:
        cursor.close()
        mydatabase.close()
