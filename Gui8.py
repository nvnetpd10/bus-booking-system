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

Label(Frame3,text="Add Bus Route Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=6,column=0)

Label(root,text="").grid(row=7,column=0)



Label(root,text="Route Id").grid(row=8,column=0,sticky=E)

a=Entry(root)
a.grid(row=8,column=1,sticky=W)



Label(root,text="station Name").grid(row=8,column=1,sticky=E)

b=Entry(root)
b.grid(row=8,column=2,sticky=W)



Label(root,text="station Id").grid(row=8,column=2,sticky=E)

c=Entry(root)
c.grid(row=8,column=3,sticky=W)

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

def add_routes():
    inp1=convert(a.get())
    inp2=b.get()
    inp3=convert(c.get())
    s="insert into routes values(%s,%s,%s)"
    tip=(inp1,inp2,inp3)
    
    
    mycursor.execute(s,tip)
    mydb.commit()
    print("addition successful")
    showinfo('Addition Successful','New route added')


Button(root,text="Add Route",bg="light green",command=add_routes).grid(row=8,column=4)

def del_route():
    inp1=convert(a.get())
    s="delete from routes where route_id=%s"
    top=(inp1,)
    mycursor.execute(s,top)
    mydb.commit()
    print('deletion successful')
    showinfo('Deletion Successful','Route deleted')

Button(root,text="Delete Route",bg="light green",fg="red",command=del_route).grid(row=8,column=5)



Label(root,text="").grid(row=9,column=0)

Label(root,text="").grid(row=10,column=0)

def gp2():
    root.destroy()
    import Gui2

pic=PhotoImage(file=".\\home.png")

Button(root,image=pic,command=gp2).grid(row=11,column=3,columnspan=2,padx=20)



