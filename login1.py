

from tkinter import *
from tkinter import messagebox
import database

class Form:
    def __init__(self,):
        self.root = Tk()
        self.root.title("User Entry Form")
        self.root.geometry('1590x1000')
        # self.root.resizable(True,True)
        
        # self.frame1 = Frame(self.root, background='#34ebab',width=600,height=450)
        # self.frame1.place(x=0,y=0)
        
        # self.label = Label(self.frame1,text='User Login',background='#34ebab',font=('arial',30))
        # self.label.place(x=235, y = 6)
        
        # self.label1 = Label(self.frame1,text='Username',background='#34ebab',font=('arial',15))
        # self.label1.place(x=170,y=90)
        
        # self.label1_ent = Entry(self.frame1,font=('arial',15))
        # self.label1_ent.place(x=280, y = 93 )
        
        # self.email = Label(self.frame1, text='Email',background='#34ebab',font=('arial',15))
        # self.email.place(x=170, y=150)
        
        # self.email_ent = Entry(self.frame1,font=('arial',15))
        # self.email_ent.place(x=280, y=150)
        
        # self.password = Label(self.frame1, text='Password', background='#34ebab',font=('arial',15))
        # self.password.place(x = 170 , y=210)
        
        # self.password_ent = Entry(self.frame1,font=('arial',15),show='#')
        # self.password_ent.place(x=280, y = 210)
        
        # self.button = Button(self.frame1,text="Save",font=('arial',15),command=self.btn_clk)
        # self.button.place(x=300, y=300)

        # lbl_bg=Label(self.root,image=self.img)
        # lbl_bg.place(x=0,y=0)
        
        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)
 

        self.frame1=lbl=Label(frame,text="Create an Account ",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.frame1.place(x=55,y=30)

        self.frame1=Label(frame,text="Username:-",font=("times new roman",18,"bold"),fg="white",bg="black")
        self.frame1.place(x=70,y=155)

        self.label1_ent = Entry(frame,font=('arial',15))
        self.label1_ent.place(x=60, y =185 )

        self.frame1=Label(frame,text="Email:-",font=("times new roman",18,"bold"),fg="white",bg="black")
        self.frame1.place(x=70,y=225)

        self.email_ent = Entry(frame,font=('arial',15))
        self.email_ent.place(x=60, y =255 )

        self.frame1=Label(frame,text="Password:-",font=("times new roman",18,"bold"),fg="white",bg="black")
        self.frame1.place(x=70,y=300)

        self.password_ent = Entry(frame,font=('arial',15),show='*')
        self.password_ent.place(x=60, y =330)

        
        # self.button = Button(frame,text="LOGIN",font=('arial',15),command=self.btn_clk,fg="white",bg="red")
        # self.button.place(x=70, y=375)

        self.button = Button(frame,text="Login",font=('arial',15),command=self.btn_clk2,fg="white",bg="red")
        self.button.place(x=180, y=375)
        
        self.button = Button(frame,text="New User",font=('arial',15),command=self.signup,fg="white",bg="red")
        self.button.place(x=48, y=375)

        # self.frame1=Label(frame,text="Username:-",font=("times new roman",18,"bold"),fg="white",bg="black")
        # self.frame1.place(x=70,y=155)

        # self.label1_ent = Entry(frame,font=('arial',15))
        # self.label1_ent.place(x=60, y =185 )

        # self.frame1=Label(frame,text="Username:-",font=("times new roman",18,"bold"),fg="white",bg="black")
        # self.frame1.place(x=70,y=155)

        # self.label1_ent = Entry(frame,font=('arial',15))
        # self.label1_ent.place(x=60, y =185 )
        

        
    def btn_clk(self):
        
        data = (self.label1_ent.get(),self.email_ent.get(),self.password_ent.get())
        print(data)
        messagebox.askokcancel("Please Select OK or Cancel")
        self.root.destroy()
        
# obj1 = Form()




    

