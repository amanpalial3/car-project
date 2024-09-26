from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image as PILImage, ImageTk
import db  # Ensure your database operations are defined in this module
import register  # Import the register module to access the registration form

class Form:
    def __init__(self,root):
        self.root = root
        self.root.title("User Entry Form")
        self.root.geometry('1590x1000')

        # Load and set the background image
        
        self.img = ImageTk.PhotoImage(PILImage.open("C:/Users/ASUS/Downloads/hbhb.webp").resize((1590, 800)))
        lbl_bg = Label(self.root, image=self.img)
        lbl_bg.place(x=0, y=0)
        



        # Create a frame for form elements
        frame = Frame(self.root, bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        title_label = Label(frame, text="Welcome to the Car Parking System", font=("Helvetica", 15), fg="white", bg='blue')
        title_label.pack(pady=20)

        title_label = Label(frame, text="LOGIN", font=("times new roman", 20, "bold"), fg="red", bg="white")
        title_label.place(x=115, y=70)

        username_label = Label(frame, text="Username:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        username_label.place(x=100, y=155)

        self.label1_ent = Entry(frame, font=('arial', 15))
        self.label1_ent.place(x=60, y=185)

        password_label = Label(frame, text="Password:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        password_label.place(x=100, y=225)

        self.password_ent = Entry(frame, font=('arial', 15), show='*')
        self.password_ent.place(x=60, y=260)

        login_button = Button(frame, text="Login", font=('arial', 15), command=self.btn_clk, bg="blue", fg="white")
        login_button.place(x=200, y=375)

        new_user_button = Button(frame, text="New User", font=('arial', 15), command=self.btn_clk1, bg="blue", fg="white")
        new_user_button.place(x=48, y=375)

        self.root.mainloop()

    def btn_clk(self):
        username = self.label1_ent.get()
        password = self.password_ent.get()
        # Perform login validation here with db
        print(username, password)
        messagebox.askokcancel("Please Select OK or Cancel")
        self.root.destroy()

    def btn_clk1(self):
        # Close the current window
        self.root.destroy()
        # Create a new instance of Tk for the registration form
        new_root = tk.Tk()  # Create a new root window for registration
        register.Form(new_root)  # Call the registration form with the new window
       

if __name__ == "__main__":
    root = tk.Tk()  # Create a Tk instance
    obj1 = Form(root)  # Pass it to the Form
    root.mainloop() 