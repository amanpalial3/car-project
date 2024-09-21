from tkinter import *
from tkinter import messagebox

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Parking Management System")
        self.root.geometry('600x400')

        # Welcome label
        self.welcome_label = Label(self.root, text="Welcome to the Car Parking Management System", font=("Arial", 20))
        self.welcome_label.pack(pady=20)

        # Button to view available parking slots
        self.view_slots_button = Button(self.root, text="View Available Parking Slots", font=("Arial", 15), command=self.view_slots)
        self.view_slots_button.pack(pady=20)

        # Button to log out
        self.logout_button = Button(self.root, text="Log Out", font=("Arial", 15), command=self.logout)
        self.logout_button.pack(pady=20)

        # Placeholder for parking slots
        self.parking_slots = [
            {"slot": 1, "status": "Available"},
            {"slot": 2, "status": "Occupied"},
            {"slot": 3, "status": "Available"},
            {"slot": 4, "status": "Occupied"},
            {"slot": 5, "status": "Available"},
        ]

    def view_slots(self):
        # Create a new window to show parking slots
        slots_window = Toplevel(self.root)
        slots_window.title("Available Parking Slots")
        slots_window.geometry('400x300')

        # Header
        header = Label(slots_window, text="Parking Slots Status", font=("Arial", 16))
        header.pack(pady=10)

        # Display each parking slot
        for slot in self.parking_slots:
            slot_label = Label(slots_window, text=f"Slot {slot['slot']}: {slot['status']}", font=("Arial", 14))
            slot_label.pack(pady=5)

    def logout(self):
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
            self.root.destroy()  # Close the dashboard
            new_root = Tk()
            Form(new_root)  # Redirect to login form

if __name__ == "__main__":
    root = Tk()
    app = Dashboard(root)
    root.mainloop()
    
 