import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image as PILImage, ImageTk
import Login
import db 

class Form:
    def __init__(self, root):
        self.root = root
        root.title("Create an Account")
        root.geometry("1590x1000")

        # Load and set the background image
        self.img = ImageTk.PhotoImage(PILImage.open("C:/Users/ASUS/Downloads/pexels-mikebirdy-170811.jpg").resize((1590, 1000)))
        lbl_bg = tk.Label(self.root, image=self.img)
        lbl_bg.place(x=0, y=0)

        # Create a frame for form elements
        self.frame = tk.Frame(self.root, bg='black', bd=5, relief=tk.RAISED)
        self.frame.place(x=10, y=100, width=480, height=450)

        title_label = tk.Label(self.frame, text="Create an Account", font=("Helvetica", 35), fg="white", bg="black")
        title_label.pack(pady=20)

        self.user_name_label = tk.Label(self.frame, text="User Name:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        self.user_name_label.place(x=50, y=100)
        self.user_name_entry = tk.Entry(self.frame, font=('arial', 16))
        self.user_name_entry.place(x=200, y=100)

        self.email_label = tk.Label(self.frame, text="Email:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        self.email_label.place(x=50, y=150)
        self.email_entry = tk.Entry(self.frame, font=('arial', 16))
        self.email_entry.place(x=200, y=150)

        self.password_label = tk.Label(self.frame, text="Password:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        self.password_label.place(x=50, y=200)
        self.password_entry = tk.Entry(self.frame, show="*", font=('arial', 16))
        self.password_entry.place(x=200, y=200)

        self.agree_var = tk.BooleanVar()
        self.agree_checkbox = ttk.Checkbutton(self.frame, text="I Agree with Terms and Conditions", variable=self.agree_var)
        self.agree_checkbox.place(x=200, y=250)

        submit_button = tk.Button(self.frame, text="Sign Up", command=self.submit_form, bg="blue", fg="white")
        submit_button.place(x=200, y=290)

        # Create the Click Me button to go to the Login page
        click_me_button = tk.Button(self.frame, text="Click Me to Login", command=self.login, bg="green", fg="white")
        click_me_button.place(x=200, y=330)

        self.root.mainloop()

    def clear_fields(self):
        """Clear the input fields."""
        self.user_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.agree_var.set(False)  # Uncheck the checkbox

    def submit_form(self):
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        data = (username, email, password)
        registration_message = db.register_user(data)

        if registration_message == "Registration successful.":
            messagebox.showinfo("Success", registration_message)
            self.clear_fields()  # Clear fields after successful registration
        else:
            messagebox.showerror("Error", registration_message)

    def login(self):
        self.root.destroy()  # Close the registration window
        new_root = tk.Tk()
        Login.form(new_root)  # Call the function to open your login page

if __name__ == "__main__":
    root = tk.Tk()
    app = Form(root)
    root.mainloop()
