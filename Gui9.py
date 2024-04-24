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

Label(Frame3,text="Add Bus Running Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)

Label(root,text="").grid(row=6,column=0)

Label(root,text="").grid(row=7,column=0)



Label(root,text="Bus ID").grid(row=8,column=2,sticky=E)

a=Entry(root)
a.grid(row=8,column=3,sticky=W)



Label(root,text="Running Date").grid(row=8,column=3,sticky=E)

b=Entry(root)
b.grid(row=8,column=4,sticky=W)



Label(root,text="Seat Available").grid(row=8,column=4,sticky=E)

c=Entry(root)
c.grid(row=8,column=5,columnspan=1,sticky=W)

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

def add_runs():
    inp1=convert(a.get())
    inp2=b.get()
    inp3=convert(c.get())
    s="insert into runs values(%s,%s,%s)"
    tip=(inp1,inp2,inp3)
    
    
    mycursor.execute(s,tip)
    mydb.commit()
    print("addition successful")
    showinfo('Addition Successful','New Run added')

Button(root,text="Add Run",bg="light green",font="Arial 10 bold",command=add_runs).grid(row=8,column=5,padx=110,sticky=W)

def del_run():
    inp1=convert(a.get())
    inp2=b.get()
    inp3=convert(c.get())
    s='delete from runs where bus_id=%s AND running_date=%s AND seats_available=%s'
    top=(inp1,inp2,inp3)
    mycursor.execute(s,top)
    mydb.commit()
    print('deletion successful')
    showinfo('Deletion Successful','Run deleted')

Button(root,text="Delete Run",bg="light green",font="Arial 10 bold",command=del_run).grid(row=8,column=5,padx=180,sticky=W)



Label(root,text="").grid(row=9,column=0)

Label(root,text="").grid(row=10,column=0)

def gp2():
    root.destroy()
    import Gui2

snap=PhotoImage(file=".\\home.png")

Button(root,image=snap,command=gp2).grid(row=11,column=4,columnspan=2)



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

