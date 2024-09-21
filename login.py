
from tkinter import *
from tkinter import messagebox
import db
from PIL import Image as PILImage, ImageTk 
import register

class Form:
    def __init__(self):
        self.root = Tk()
        self.root.title("User Entry Form")
        self.root.geometry('1590x1000')



        self.img = ImageTk.PhotoImage(PILImage.open("C:/Users/ASUS/Downloads/chuttersnap-gts_Eh4g1lk-unsplash.jpg").resize((1590, 1000)))


        lbl_bg=Label(self.root,image=self.img)
        lbl_bg.place(x=0,y=0)


        # Create a frame for form elements
        frame = Frame(self.root, bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        title_label = Label(frame, text="Create an Account", font=("times new roman", 20, "bold"), fg="red", bg="white")
        title_label.place(x=55, y=30)

        username_label = Label(frame, text="Username:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        username_label.place(x=70, y=155)

        self.label1_ent = Entry(frame, font=('arial', 15))
        self.label1_ent.place(x=60, y=185)

        email_label = Label(frame, text="Email:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        email_label.place(x=70, y=225)

        self.email_ent = Entry(frame, font=('arial', 15))
        self.email_ent.place(x=60, y=255)

        password_label = Label(frame, text="Password:", font=("times new roman", 18, "bold"), fg="white", bg="black")
        password_label.place(x=70, y=300)

        self.password_ent = Entry(frame, font=('arial', 15), show='*')
        self.password_ent.place(x=60, y=330)

        login_button = Button(frame, text="Login", font=('arial', 15), command=self.btn_clk, fg="red", bg="black")
        login_button.place(x=200, y=375)

        new_user_button = Button(frame, text="New User", font=('arial', 15), command=self.btn_clk1, fg="red", bg="black")
        new_user_button.place(x=48, y=375)

        self.root.mainloop()

    def btn_clk(self):
        data = (self.label1_ent.get(), self.email_ent.get(), self.password_ent.get())
        print(data)
        messagebox.askokcancel("Please Select OK or Cancel")
        self.root.destroy()

    def btn_clk1(self):
        data = (self.label1_ent.get(), self.email_ent.get(), self.password_ent.get())
        print(data)
        self.root.destroy()

if __name__ == "__main__":
    obj1 = Form()





    

