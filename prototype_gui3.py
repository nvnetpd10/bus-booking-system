from datetime import datetime
from tkinter import messagebox
from tkinter import *

from tkinter.messagebox import askyesno
import mysql.connector as sql

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
def refresh():
    root.destroy()
    import prototype_gui3
Button(root,text="REFESH",command=refresh).pack(side=TOP,anchor=NW)

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
        import Gui10

image=PhotoImage(file=".\\home.png")
def home():
    root.destroy()
    import Gui2

Button(tframe,image=image,command=home).pack(side=LEFT,anchor=N)
#print(v.get())

root.mainloop()

