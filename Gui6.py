from tkinter import *
import mysql.connector as sql
from tkinter import messagebox
from tkinter.messagebox import *
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

Label(Frame3,text="Add Bus Operator Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=6,column=0)

Label(root,text="").grid(row=7,column=0)



Label(root,text="Operator id").grid(row=8,column=0,sticky=E)

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


a=Entry(root)
a.grid(row=8,column=1,sticky=W)



Label(root,text="Name").grid(row=8,column=1,sticky=E)

b=Entry(root)
b.grid(row=8,column=2,sticky=W)



Label(root,text="Address").grid(row=8,column=2,sticky=E)

c=Entry(root)
c.grid(row=8,column=3,sticky=W)



Label(root,text="Phone").grid(row=8,column=3,sticky=E)

d=Entry(root)
d.grid(row=8,column=4,sticky=W)



Label(root,text="Email").grid(row=8,column=4,sticky=E)

e=Entry(root)
e.grid(row=8,column=5,sticky=W)


def add_entry():
    inp1=convert(a.get())
    inp2=b.get()
    inp3=c.get()
    inp4=convert(d.get())
    inp5=e.get()
    s="insert into operators values(%s,%s,%s,%s,%s)"
    tip=(inp1,inp2,inp3,inp4,inp5)
    
    
    mycursor.execute(s,tip)
    mydb.commit()
    print("addition successful")
    showinfo('Addition Successful','New operator added')

Button(root,text="Add",bg="light green",command=add_entry).grid(row=8,column=5,columnspan=2)

def edit_entry():
    inp1=convert(a.get())
    inp2=b.get()
    inp3=c.get()
    inp4=convert(d.get())
    inp5=e.get()
    s="update operators set name=%s, address=%s, phone_no=%s, email=%s where o_id=%s"
    top=(inp2,inp3,inp4,inp5,inp1)
    mycursor.execute(s,top)
    mydb.commit()
    print("edit successful")
    showinfo('Editing Successful','Operator edited ')

Button(root,text="Edit",bg="light green",command=edit_entry).grid(row=8,column=5,columnspan=3)



Label(root,text="").grid(row=9,column=0)

Label(root,text="").grid(row=10,column=0)

def gp2():
    root.destroy()
    import Gui2

photo=PhotoImage(file=".\\home.png")

Button(root,image=photo,command=gp2).grid(row=11,column=4,columnspan=2)





