from datetime import datetime
from datetime import *
from tkinter import messagebox
import tkinter as tk
from tkinter.messagebox import *
from tkinter import *
import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='RsA%9V27',
    database = 'bus_booking'
    #use_pure=True
)
class booking_system():
    def Gui1(self):
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
            self.Gui2()

        root.after(1000,gp2)


    def Gui2(self):
        root=Tk()



        w,h=root.winfo_screenwidth(),root.winfo_screenheight()



        root.geometry('%dx%d+0+0'%(w,h))



        img=PhotoImage(file='.\\Bus_for_project.png')



        Label(root,image=img).grid(row=0,column=0,padx=400,columnspan=7)



        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=40)

        def gp3():
            root.destroy()
            self.prototype_gui3()

        Button(root,text='Seat Booking',bg='LightGreen',font="Arial 14 bold",command=gp3).grid(row=5,column=1,padx=80,columnspan=2)

        def gp4():
            root.destroy()
            self.Gui4_2()

        Button(root,text='Check Booked seat',bg='green2',font="Arial 14 bold",command=gp4).grid(row=5,column=2,padx=60,columnspan=3)

        def gp5():
            root.destroy()
            self.Gui5()

        Button(root,text='Add Bus details',bg='green4',font="Arial 14 bold",command=gp5).grid(row=5,column=3,columnspan=4)



        Label(root,text="").grid(row=6,column=2)



        admin=Label(root,text="For Admin Only",fg="red",font="Arial 8 bold").grid(row=7,column=3,columnspan=4)


        root.mainloop()

    def Gui5(self):

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
            self.Gui6()

        Button(root,text="New Operator",bg="pale green",command=gp6).grid(row=7,column=0,columnspan=7)

        def gp7():
            root.destroy()
            self.Gui7()

        Button(root,text="New Bus",bg="salmon",command=gp7).grid(row=7,column=1,columnspan=7)

        def gp8():
            root.destroy()
            self.Gui8()

        Button(root,text="New Route",bg="SteelBlue3",command=gp8).grid(row=7,column=2,columnspan=7)

        def gp9():
            root.destroy()
            self.Gui9()

        Button(root,text="New Run",bg="MistyRose3",command=gp9).grid(row=7,column=3,columnspan=7)

    def Gui6(self):
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
            self.Gui2()

        photo=PhotoImage(file=".\\home.png")

        Button(root,image=photo,command=gp2).grid(row=11,column=4,columnspan=2)


    def Gui7(self):


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
            self.Gui2()

        photo=PhotoImage(file=".\\home.png")

        Button(root,image=photo,command=gp2).grid(row=11,column=5,sticky=W)

    def Gui8(self):

        

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
            self.Gui2()

        pic=PhotoImage(file=".\\home.png")

        Button(root,image=pic,command=gp2).grid(row=11,column=3,columnspan=2,padx=20)



    def Gui9(self):

                
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
            self.Gui2()

        snap=PhotoImage(file=".\\home.png")

        Button(root,image=snap,command=gp2).grid(row=11,column=4,columnspan=2)



        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

    def Gui10(self):

                
        mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='RsA%9V27',
            database = 'bus_booking'
            #use_pure=True
        )

        mycursor=mydb.cursor()

        mycursor.execute("select * from passengers order by booking_ref desc")
        ftabu=mycursor.fetchall()[0]
        print(ftabu)


        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.state('zoomed')
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=10)
        Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=10)
        Label(root,text='Bus Ticket',font="Arial 15 bold",fg='black').grid(row=2,column=0,columnspan=10,pady=h//20)
        final=LabelFrame(root)
        final.grid(row=8,column=3,columnspan=3)
        Label(final, text='Passenger: '+str(ftabu[1])).grid(row=8,column=0)
        Label(final, text='No of Seats: '+str(ftabu[4])).grid(row=9,column=0)
        Label(final, text='Age: '+str(ftabu[2])).grid(row=10,column=0)
        Label(final, text='Booking Ref: '+str(ftabu[0])).grid(row=11,column=0)
        Label(final, text='Travels on: '+str(ftabu[9])).grid(row=12,column=0)
        Label(final, text='Final destination: '+str(ftabu[7])).grid(row=13,column=0)
        Label(final, text='Gender: '+str(ftabu[3])).grid(row=8,column=1)
        Label(final, text='Phone: '+str(ftabu[5])).grid(row=9,column=1)
        Label(final, text='Phone: '+str(ftabu[5])).grid(row=9,column=1)
        Label(final, text='Fare Rs: '+str(ftabu[11])).grid(row=10,column=1)
        Label(final, text='Bus details: '+str(ftabu[10])).grid(row=11,column=1)
        Label(final, text='Booked On: '+str(date.today())).grid(row=12,column=1)
        Label(final, text='Boarding Point: '+str(ftabu[6])).grid(row=13,column=1)
        Label(final, text='Total amount Rs '+str(ftabu[11])+' to be paid at the time of boarding the bus: ',font='arial 8 italic ',fg='grey').grid(row=14,column=1)
        showinfo('success','seat booked')
        def on_closing():
            direct=askyesnocancel("closing","for closing click yes \n to go to main page click no")
            if direct==True:
                showinfo('Thanks','Thank you for using python bus service')
                root.destroy()
            elif direct==False:
                root.destroy()
                self.Gui2()



        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

    def prototype_gui3(self):

                
        mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='RsA%9V27',
            database = 'bus_booking'
            #use_pure=True
        )

        mycursor=mydb.cursor()
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


        root=Tk()

        tframe=Frame(root)
        tframe.pack(side=TOP)

        bframe=Frame(root)
        bframe.pack(side=TOP)

        root.state("zoomed")


        img=PhotoImage(file='.\\Bus_for_project.png')



        Label(tframe,image=img).pack(side=TOP)



        Label(tframe,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").pack(side=TOP)



        Label(tframe,text="Enter Journey Details",bg="light green",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").pack(side=TOP)



        #Label(root,text="").grid(row=4,column=0)

        Label(tframe,text="To").pack(side=LEFT,anchor=N,padx=(100,0))

        fd=Entry(tframe)
        fd.pack(side=LEFT,anchor=N)





        Label(tframe,text="From").pack(side=LEFT,anchor=N)

        src=Entry(tframe)
        src.pack(side=LEFT,anchor=N)





        Label(tframe,text="Journey Date").pack(side=LEFT,anchor=N)


        dt=Entry(tframe)
        dt.pack(side=LEFT,anchor=N)

        rb=0
        ftup=[]
        shed={}
        def radio():
            global rb
            rb=v.get()
            print(v.get())
            #ftup=shed[rb]
            
            
        frameNew=Frame(root)
        frameNew.pack(side=TOP)
        frame1=Frame(root,height=500)
        frame1.pack(side=LEFT,anchor=N,padx=(550,0))
        frame2=Frame(root,height=500)
        frame2.pack(side=LEFT,anchor=N)
        frame3=Frame(root,height=500)
        frame3.pack(side=LEFT,anchor=N)
        frame4=Frame(root,height=500)
        frame4.pack(side=LEFT,anchor=N)
        frame5=Frame(root,height=500)
        frame5.pack(side=LEFT,anchor=N)
        v = IntVar()
            
        def show_buses():
            a=fd.get()
            b=src.get()
            c=dt.get()
            mycursor.execute("select * from buses B join runs R on B.bus_id=R.bus_id")
            bd=mycursor.fetchall()  
            mycursor.execute("select * from routes")
            rd=mycursor.fetchall()
            mycursor.execute("select * from operators")
            opd=mycursor.fetchall()
            #date_str = '09-19-2018'
            
            #v.set("2")
            counter =0
            
            d_obj = datetime.strptime(c, '%Y-%m-%d').date()
            print("operator"+"\t"+"bus type"+"\t"+"available/capacity"+"\t"+"fare ")
            
            
            
            
            Label(frame1,text="Bus",fg="green",font="Arial 11").pack(side=TOP,padx=5)
            Label(frame2,text="Operator",fg="green",font="Arial 11").pack(side=TOP,padx=5)
            Label(frame3,text="Bus_Type",fg="green",font="Arial 11").pack(side=TOP,padx=5)
            Label(frame4,text="Available/Capacity",fg="green",font="Arial 11").pack(side=TOP,padx=5)
            Label(frame5,text="Fare",fg="green",font="Arial 11").pack(side=TOP,padx=5)
           
            
            for i in rd:
                for j in rd:
                    for k in bd:
                        if((i[1]==b and j[1]==a) and i[0]==j[0] and k[7]==d_obj and k[5]==i[0]):
                            for l in opd:
                                if(l[0]==k[4]):
                                    op_name=l[1]
                            if k[8]==0:
                                continue
                            
                            counter=counter+1
                            Radiobutton(frame1, text = ("bus"+str(counter)), variable = v,
                            value = counter,indicator =0,
                            background = "light blue",command=radio).pack(side=TOP,padx=5)
                            l=str(op_name)
                            
                            disp=str(op_name)+" "+str(k[1])+" "+str(k[8])+"/"+str(k[2])+" "+str(k[3])
                            Label(frame2,text=op_name,fg="blue",font="Arial 11").pack(side=TOP,padx=5)
                            Label(frame3,text=str(k[1]),fg="blue",font="Arial 11").pack(side=TOP,padx=5)
                            Label(frame4,text=str(k[8])+'/'+str(k[2]),fg="blue",font="Arial 11").pack(side=TOP,padx=5)
                            Label(frame5,text=str(k[3]),fg="blue",font="Arial 11").pack(side=TOP,padx=5)
                            
                            '''Label(frame,text=str(k[1]),fg="green",font="Arial 14").pack(relx=0.14,rely=0.10,anchor=NW)
                            Label(frame2,text=str(k[8]),fg="green",font="Arial 14").pack(relx=0.16,rely=0.10,anchor=NW)
                            Label(frame2,text=str(k[2]),fg="green",font="Arial 14").pack(relx=0.18,rely=0.10,anchor=NW)
                            Label(frame2,text=str(k[3]),fg="green",font="Arial 14").pack(relx=0.20,rely=0.10,anchor=NW)'''
                            allinfo=[op_name,k[0],k[1],k[8],k[2],k[3]]
                            
                            shed[counter]=allinfo


                            #Label(frame2,text="    "+disp,font="Arial 18").pack(side=tk.LEFT)
            
            global rb
            #rb=v.get()
            
            #print(rb)
            #print(ftup)

            Button(frameNew,text="Proceed to book", bg='SpringGreen2', font='Arial 13 bold',command=lambda:fill_detail(ftup,a,b,c,d_obj)).pack(side=TOP)
            
            

        framef=Frame(root)
        framef.place(x=300,y=600)
        def fill_detail(ftup,a,b,c,d_obj):
            Label(framef,text="Fill Passenger Details", bg='CadetBlue1', fg='red', font='Arial 20 bold').pack(side=TOP,pady=30)
            Label(framef,text="Name", font='Arial 10 bold').pack(side=LEFT)
            name=Entry(framef)
            name.pack(side=LEFT)
            
            Gen=StringVar()
            Gen.set("Select Gender")
         
            option=["Male","Female","Third Gender"]
            menu=OptionMenu(framef,Gen,*option)
            menu.pack(side=LEFT)
            Label(framef,text="no. of seats", font='Arial 10 bold').pack(side=LEFT)
            nos=Entry(framef)
            nos.pack(side=LEFT)
            
            Label(framef,text="Mobile no.", font='Arial 10 bold').pack(side=LEFT)
            phone=Entry(framef)
            phone.pack(side=LEFT)
            Label(framef,text="Age", font='Arial 10 bold').pack(side=LEFT)
            age=Entry(framef)
            age.pack(side=LEFT)
            
            Button(framef,text="Book seat", font='Arial 11 bold',bg='SpringGreen2',command=lambda:make_ticket(ftup,a,b,c,name,Gen,menu,nos,phone,age,d_obj)).pack(side=LEFT)
            
            
            
            
                            
            
            
        Button(tframe,text="Show Bus",bg="SpringGreen3",font="Arial 10 bold",command=show_buses).pack(side=LEFT,anchor=N)

        def make_ticket(ftup,a,b,c,name,Gen,menu,nos,phone,age,d_obj):
            print(rb)
            print(shed)
            ftup=shed[rb]
            if(convert(nos.get())>ftup[3]):
                messagebox.showerror('Error', 'Error: Cannot book more seats than available!')
                return
            mycursor.execute("select count(*) from passengers")
            ticket_no=mycursor.fetchall()[0][0]
            pname=name.get()
            page=convert(age.get())
            pgen=Gen.get()
            pnos=convert(nos.get())
            pphone=convert(phone.get())
            ps=b
            pd=a
            var1=ftup[0]
            bid=ftup[1]
            money=ftup[5]*pnos

            answer = askyesno(title='Fare confirm',
                            message='Total amount to be paid is '+str(money))
            if answer:
            
                quer="insert into passengers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                ptup=(ticket_no,pname,page,pgen,pnos,pphone,b,a,bid,d_obj,var1,money)
                mycursor.execute(quer,ptup)
                mydb.commit()
                q2="update runs set seats_available=%s where bus_id=%s AND running_date=%s"
                san=ftup[3]-pnos
                t2=(san,bid,d_obj)
                mycursor.execute(q2,t2)
                mydb.commit()
                print(type(ticket_no),type(pname),type(page),type(pgen),type(pnos),type(pphone),type(b),type(a),type(bid),type(d_obj),type(var1))
                root.destroy()
                self.Gui10()

        image=PhotoImage(file=".\\home.png")
        def home():
            root.destroy()
            self.Gui2()

        Button(tframe,image=image,command=home).pack(side=LEFT,anchor=N)
        #print(v.get())

        root.mainloop()

    def Gui4_2(self):

        mydb = sql.connect(
            host='localhost',
            user='root',
            passwd='RsA%9V27',
            database = 'bus_booking' )

        mycursor=mydb.cursor()


        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=10)
        Label(root,text='Online Bus Booking System',font="Arial 24 bold", bg='light blue',fg='red').grid(row=1,column=0,columnspan=10)
        Label(root,text='Check Your Booking',font="Arial 18 bold", bg='light green',fg='green').grid(row=2,column=0,columnspan=10,pady=h//20)
        Label(root,text='Enter Your Mobile No',font="Arial 12 bold",fg='black').grid(row=3,column=4)
        var1=Entry(root)
        var1.grid(row=3,column=5)


        def confirm():
            answer = askyesno(title='no booking record',
                            message='would you like to book now?')
            if answer:
                root.destroy()
                self.prototype_gui3()

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

        def info():
            if len(str(var1.get()))==0:
                showerror('ERROR', 'Enter mobile number!')
                root.destroy()
                self.Gui4_2()
            q1='select * from passengers where phone_no=%s'
            cfn=convert(var1.get())
            t1=(cfn,)
            mycursor.execute(q1,t1)
            r2=mycursor.fetchone()
            if r2==None:
                confirm()
            else:
                
                final=LabelFrame(root)
                final.grid(row=8,column=4,columnspan=3)
                Label(final, text='Passenger: '+str(r2[1])).grid(row=8,column=0)
                Label(final, text='No of Seats: '+str(r2[4])).grid(row=9,column=0)
                Label(final, text='Age: '+str(r2[2])).grid(row=10,column=0)
                Label(final, text='Booking Ref.9: '+str(r2[0])).grid(row=11,column=0)
                Label(final, text='Travels on: '+str(r2[9])).grid(row=12,column=0)
                Label(final, text='Final destination: '+str(r2[7])).grid(row=13,column=0)
                Label(final, text='Gender: '+str(r2[3])).grid(row=8,column=1)
                Label(final, text='Phone: '+str(r2[5])).grid(row=9,column=1)
                Label(final, text='Phone: '+str(r2[5])).grid(row=9,column=1)
                Label(final, text='Fare Rs: '+str(r2[11])).grid(row=10,column=1)
                Label(final, text='Bus details: '+str(r2[10])).grid(row=11,column=1)
                Label(final, text='Booked On: '+str(date.today())).grid(row=12,column=1)
                Label(final, text='Boarding Point: '+str(r2[6])).grid(row=13,column=1)
                Label(final, text='Total amount Rs '+str(r2[11])+ 'to be paid at the time of boarding he bus: ',fg='grey').grid(row=14,column=1)
        Button(root,text='Check Booking',command=info,font="Arial 12 bold ",fg='black').grid(row=3,column=6)
obj=booking_system()
obj.Gui1()







        


