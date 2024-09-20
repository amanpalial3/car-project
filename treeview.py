from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import database

class Treeview:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Treeview")
        self.root.geometry('700x500')
        
        self.table = ttk.Treeview(self.root,columns=['id','username','email','password','edit','delete'],show='headings')
        self.table.pack()
        
        self.table.heading("#1",text="Id")
        self.table.heading("#2",text="Username")
        self.table.heading("#3",text="Email")
        self.table.heading("#4",text="Password")
        self.table.heading("#5",text="Edit")
        self.table.heading("#6",text="Delete")
        
        # self.table.column(width=)
        
        
        response = database.get_all()
        print(response)
        
        for data in response:
            self.table.insert("",0,text=data[0],values=[data[0],data[1],data[2],data[3],'Edit','Delete'])
        

       
        self.root.mainloop()
        
obj1 = Treeview()
