from tkinter import *



root=Tk()



w,h=root.winfo_screenwidth(),root.winfo_screenheight()



root.geometry('%dx%d+0+0'%(w,h))



img=PhotoImage(file='.\\Bus_for_project.png')



Label(root,image=img).grid(row=0,column=0,padx=400,columnspan=7)



Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=40)

def gp3():
    root.destroy()
    import prototype_gui3

Button(root,text='Seat Booking',bg='LightGreen',font="Arial 14 bold",command=gp3).grid(row=5,column=1,padx=80,columnspan=2)

def gp4():
    root.destroy()
    import Gui4_2

Button(root,text='Check Booked seat',bg='green2',font="Arial 14 bold",command=gp4).grid(row=5,column=2,padx=60,columnspan=3)

def gp5():
    root.destroy()
    import Gui5

Button(root,text='Add Bus details',bg='green4',font="Arial 14 bold",command=gp5).grid(row=5,column=3,columnspan=4)



Label(root,text="").grid(row=6,column=2)



admin=Label(root,text="For Admin Only",fg="red",font="Arial 8 bold").grid(row=7,column=3,columnspan=4)


root.mainloop()




