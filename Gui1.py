from tkinter import *



root=Tk()



w,h=root.winfo_screenwidth(),root.winfo_screenheight()



root.geometry('%dx%d+0+0'%(w,h))



img=PhotoImage(file='.\\Bus_for_project.png')



Label(root,image=img).pack()



Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()



Label(root,text='Name : Mrinmoy Sadhukhan',fg='blue2',font="Arial 11 bold",pady=25).pack()



Label(root,text='Er : 211B188',fg='blue2',font="Arial 11 bold",pady=25).pack()



Label(root,text='Mobile : 8789343317 ',fg='blue2',font="Arial 11 bold",pady=25).pack()



Label(root,text='Submitted to : Dr. Mahesh Kumar and Dr. Nilesh Patel',fg='Red',bg='LightBlue1',font="Arial 15 bold").pack()



Label(root,text='Project Based Learning',fg='Red',font="Arial 13 bold").pack()

def gp2():
    root.destroy()
    import Gui2

root.after(10000,gp2)

