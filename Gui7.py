from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='RsA%9V27',
    database = 'bus_booking'
    #use_pure=True
)

mycursor=mydb.cursor()


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



Frame3=Frame(root)

Frame3.grid(row=5,column=0,columnspan=10)

Label(Frame3,text="Add Bus Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=6,column=0)

Label(root,text="").grid(row=7,column=0)



Label(root,text="Bus ID").grid(row=8,column=0,sticky=E)

a=Entry(root)
a.grid(row=8,column=1,sticky=W)



Label(root,text="Bus Type").grid(row=8,column=1,sticky=E)

bus=StringVar()

bus.set("Select")

option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non-AC sleeper 2x1"]

menu=OptionMenu(root,bus,*option)

menu.grid(row=8,column=2,sticky=W)




Label(root,text="Capacity").grid(row=8,column=2,sticky=E)

c=Entry(root)
c.grid(row=8,column=3,sticky=W)



Label(root,text="Fare Rs").grid(row=8,column=3,sticky=E)

d=Entry(root)
d.grid(row=8,column=4,sticky=W)



Label(root,text="Operator Id").grid(row=8,column=4,sticky=E)

e=Entry(root)
e.grid(row=8,column=5,sticky=W)


Label(root,text="Route Id").grid(row=8,column=5,sticky=E)

f=Entry(root)
f.grid(row=8,column=6,sticky=W)



Label(root,text="").grid(row=9,column=0)

Label(root,text="").grid(row=10,column=0)

def digi(z):
    if(z=='1'):
        return 1
    if(z=='2'):
        return 2
    if(z=='3'):
        return 3
    if(z=='4'):
        return 4
    if(z=='5'):
        return 5
    if(z=='6'):
        return 6
    if(z=='7'):
        return 7
    if(z=='8'):
        return 8
    if(z=='9'):
        return 9
    if(z=='0'):
        return 0
def convert(s):
    num=0
    for i in s:
        num=num*10
        j=digi(i)
        num=num+j
    return num


def add_bus():
    inp2=bus.get()
    inp1=convert(a.get())
    inp3=convert(c.get())
    inp4=convert(d.get())
    inp5=convert(e.get())
    inp6=convert(f.get())
    s="insert into buses values(%s,%s,%s,%s,%s,%s)"
    tip=(inp1,inp2,inp3,inp4,inp5,inp6)
    
    
    mycursor.execute(s,tip)
    mydb.commit()
    print("addition successful")
    showinfo('Addition Successful','New bus added')

Button(root,text="Add Bus",bg="light green",command=add_bus).grid(row=11,column=3,sticky=E,padx=20)

def edit_bus():
    inp2=bus.get()
    inp1=convert(a.get())
    inp3=convert(c.get())
    inp4=convert(d.get())
    inp5=convert(e.get())
    inp6=convert(f.get())
    s="update buses set bus_type=%s, capacity=%s, fare=%s, op_id=%s, r_id=%s where bus_id=%s"
    top=(inp2,inp3,inp4,inp5,inp6,inp1)
    mycursor.execute(s,top)
    mydb.commit()
    print('edit successful')
    showinfo('Editing Successful','Bus info edited')

Button(root,text="Edit Bus",bg="light green",command=edit_bus).grid(row=11,column=4,columnspan=1,sticky=W)

def gp2():
    root.destroy()
    import Gui2

photo=PhotoImage(file=".\\home.png")

Button(root,image=photo,command=gp2).grid(row=11,column=5,sticky=W)









