import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image as PILImage, ImageTk

class Form:
    def __init__(self, root):
        self.root = root
        root.title("Create an Account")
        root.geometry("1590x1000")

        title_label = tk.Label(root, text="Create an Account", font=("Helvetica", 35))
        title_label.pack(pady=100)

        self.user_name_label = tk.Label(root, text="User Name:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        self.user_name_label.place(x=500, y=256)
        self.user_name_entry = tk.Entry(root, font=('arial', 16))
        self.user_name_entry.place(x=665, y=256)

        self.password_label = tk.Label(root, text="Password:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        self.password_label.place(x=500, y=300)
        self.password_entry = tk.Entry(root, show="*", font=('arial', 16))
        self.password_entry.place(x=665, y=300)

        self.retype_password_label = tk.Label(root, text="Retype Password:", font=("times new roman", 15, "bold"), fg="white", bg="black")
        self.retype_password_label.place(x=500, y=345)
        self.retype_password_entry = tk.Entry(root, show="*", font=('arial', 18))
        self.retype_password_entry.place(x=665, y=345)

        self.email_label = tk.Label(root, text="Email:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        self.email_label.place(x=500, y=390)
        self.email_entry = tk.Entry(root, font=('arial', 18))
        self.email_entry.place(x=665, y=390)

        self.agree_var = tk.BooleanVar()
        self.agree_checkbox = ttk.Checkbutton(root, text="I Agree with Terms and Conditions", variable=self.agree_var)
        self.agree_checkbox.place(x=665, y=440)

        submit_button = tk.Button(root, text="Sign Up", command=self.submit_form)
        submit_button.place(x=665, y=470)

        # Create the Click Me button to go to the Login page
        click_me_button = tk.Button(root, text="Click Me to Login", command=self.go_to_login)
        click_me_button.place(x=665, y=510)

    def submit_form(self):
        user_name = self.user_name_entry.get()
        password = self.password_entry.get()
        retype_password = self.retype_password_entry.get()
        email = self.email_entry.get()

        if user_name == "" or password == "" or retype_password == "" or email == "":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != retype_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        messagebox.showinfo("Success", f"Account created for {user_name}!")

    def go_to_login(self):
        self.root.destroy()  # Close the registration window
        import login  # Import the login module
        login.Form()  # Call the function to open your login page

if __name__ == "__main__":
    root = tk.Tk()
    app = Form(root)
    root.mainloop()
