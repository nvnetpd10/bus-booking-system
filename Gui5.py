from tkinter import *

root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file=".\\Bus_for_project.png")

Frame1=Frame(root)

Frame1.grid(row=0,column=0,columnspan=10)

Label(Frame1,image=img).grid(row=0,column=0,padx=600,columnspan=7)

Label(root,text="").grid(row=2,column=0)



Frame2=Frame(root)

Frame2.grid(row=3,column=0,columnspan=10)

Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=4,column=0)



Frame_3=Frame(root)

Frame_3.grid(row=5,column=0,columnspan=10)

Label(Frame_3,text="Add New Details to DataBase ",fg="green4",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=6,column=0)

def gp6():
    root.destroy()
    import Gui6

Button(root,text="New Operator",bg="pale green",command=gp6).grid(row=7,column=0,columnspan=7)

def gp7():
    root.destroy()
    import Gui7

Button(root,text="New Bus",bg="salmon",command=gp7).grid(row=7,column=1,columnspan=7)

def gp8():
    root.destroy()
    import Gui8

Button(root,text="New Route",bg="SteelBlue3",command=gp8).grid(row=7,column=2,columnspan=7)

def gp9():
    root.destroy()
    import Gui9

Button(root,text="New Run",bg="MistyRose3",command=gp9).grid(row=7,column=3,columnspan=7)



