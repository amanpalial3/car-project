from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import database1

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
        
        
        response = database1.get_all()
        print(response)
        
        for data in response:
            self.table.insert("",0,text=data[0],values=[data[0],data[1],data[2],data[3],'Edit','Delete'])
            
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        self.table.bind('<Double-Button-1>',self.action)
        self.table.pack()
        
       
        self.root.mainloop()
        
    def action(self,n):
        print("Action")
        print(self.table.focus())
        tf = self.table.focus()
        col =self.table.identify_column(n.x)
        print(col)
        rowid =( self.table.item(tf).get('text'),)
        print(rowid)
        
        if col == '#6':
            response = messagebox.askyesno("Delete, Are you sure ?")
            if response:
                result = database1.deleteuser(rowid)
                if result:
                    messagebox.showinfo("Data is deleteed...")
                    self.root.destroy()
                    Treeview()
                else:
                    messagebox.showerror('Someting went wrong ?')
  
        
if __name__=='__main__':
    Treeview()