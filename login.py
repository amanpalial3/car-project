from tkinter import *
from tkinter import messagebox
import database1
from PIL import Image as PILImage, ImageTk 
import register


class Form:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry('1590x1000')
        # self.root.resizable(FALSE,False)
         
        # self.img=ImageTk.PhotoImage(file="C:/Users/ASUS/Downloads/sergei-gussev-Ugf4r01cDPQ-unsplash.jpg")
        self.img = ImageTk.PhotoImage(PILImage.open("C:/Users/ASUS/Downloads/chuttersnap-gts_Eh4g1lk-unsplash.jpg").resize((1590, 1000)))


        lbl_bg=Label(self.root,image=self.img)
        lbl_bg.place(x=0,y=0)
        
        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)
 

        self.frame1=lbl=Label(frame,text="Car Parking Slot Booking ",font=("times new roman",20,"bold"),fg="red",bg="white")
        self.frame1.place(x=14,y=30)

        self.frame1=Label(frame,text="LOGIN",font=("times new roman",18,"bold"),fg="white",bg="black")
        self.frame1.place(x=120,y=105)

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



        
        self.root.mainloop()

    def signup(self):
     self.root.destroy()
     new_root = Tk()
     register.Form(new_root)  # Ensure this is calling the correct Form class


        
    def login(self):
        email = self.email_ent.get()
        password = self.password_ent.get()
        response = database1.login_user((email, password))

        if response:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            dashboard_root = Tk()
            Dashboard(dashboard_root)
        else:
            messagebox.showerror("Error", "Invalid email or password.")

if __name__=="__main__":
     root = Tk()
     app = Form(root)
     root.mainloop()



   