
from tkinter import *
from tkcalendar import Calendar


root = Tk()
root.title("Calender")
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',year = 2023, month = 8,day = 1)
cal.pack(pady = 20,side="top")
lbl = Label(root, text = "Select Date And Press Check ",background="light green")
lbl.pack()
frame = Frame(root)
frame.pack()

# many time click button
def grad_date():
	date.config(text="Date is: "+cal.get_date())
Button(root,text="Get Date",command=grad_date,background="light blue").pack(pady = 20)
date = Label(root, text = "")
date.pack(pady = 20)
root.mainloop()
