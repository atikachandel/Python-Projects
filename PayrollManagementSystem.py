#start
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sql")
mycursor=mydb.cursor()
mycursor.execute("create database CP")

#creation_of_table

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sql",database="CP")
mycursor=mydb.cursor()
mycursor.execute("create table payroll(Sr_no int(4) primary key,\
                 Name varchar(30),\
                 Adr varchar(30),\
                 City varchar(20),\
                 P_C int,\
                 Salary int,\
                 DA int,\
                 O_T int,\
                 Pension int,\
                 P_D char(40),\
                 J_C  int,\
                 Shift varchar(40),\
                 D_S int,\
                 W_E char(40),\
                 BG char(40),\
                 Gender varchar(20),\
                 Mo_no int,\
                 Post varchar(40),\
                 Dept varchar(40),\
                 Age int,\
                 E_A char(100))") 


#show_tables

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sql",database="CP")
mycursor=mydb.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)

#values

#1
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             password="sql",\
                             database="CP")
mycursor=mydb.cursor()
sql="insert into payroll (Sr_no,Name,Adr,City,P_C,Salary,DA,O_T,Pension,P_D,J_C,Shift,D_S,W_E,BG,Gender,Mo_no,Post,Dept,Age,E_A)\
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(1,'AVI','GANJ','LKO',226,1000,20,10,500,"10-05-20","I",856,00,"2 YRS","O+","MALE",9235632355,"RECEPTIONIST","CARDIOLOGY",32,"abhi1@gmail.com")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recorded")

#2
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             password="sql",\
                             database="CP")
mycursor=mydb.cursor()
sql="insert into payroll (Sr_no,Name,Adr,City,P_C,Salary,DA,O_T,Pension,P_D,J_C,Shift,D_S,W_E,BG,Gender,Mo_no,Post,Dept,Age,E_A)\
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(2,'ABHI','GANJ','LKO',225,2000,10,20,530,"11-05-2020",817,'II',10,"5 YRS","A+","MALE",955234555,"SWEEPER","CARDIOLOGY",32,"abhi123@gmail.com")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recorded")

#3
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             password="sql",\
                             database="CP")
mycursor=mydb.cursor()
sql="insert into payroll (Sr_no,Name,Adr,City,P_C,Salary,DA,O_T,Pension,P_D,J_C,Shift,D_S,W_E,BG,Gender,Mo_no,Post,Dept,Age,E_A)\
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(3,'ANU','VKS ROAD','LKO',213,5000,30,30,100,"11-05-2020",932,'I',00,"3 YRS","O+",'FEMALE',911112355,"RECEPTIONIST","OPTHAMOLOGY",22,"anu1@gmail.com")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recorded")

#4
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             password="sql",\
                             database="CP")
mycursor=mydb.cursor()
sql="insert into payroll values(Sr_no,Name,Adr,City,P_C,Salary,DA,O_T,Pension,P_D,J_C,Shift,D_S,W_E,BG,Gender,Mo_no,Post,Dept,Age,E_A)\
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(4,'ANITA','ALIGANJ','LKO',242,4000,20,10,500,"10-05-2020",631,'II',10,"5 YRS","B+",'FEMALE',9678632354,"WORKER","CARDIOLOGY",31,"anita334@gmail.com")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recorded")

#5
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             password="sql",\
                             database="CP")
mycursor=mydb.cursor()
sql="insert into payroll values(Sr_no,Name,Adr,City,P_C,Salary,DA,O_T,Pension,P_D,J_C,Shift,D_S,W_E,BG,Gender,Mo_no,Post,Dept,Age,E_A)\
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(5,'RAMESH','SP MARG','LKO',225,1000,30,10,100,"17-05-2020",764,'II',00,"10 YRS","AB+","MALE",9231232324,"SWEEPER","UREOLOGY",41,"ramesh8@gmail.com")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"recorded")

#tkinter_file

from tkinter import*
import random
import time
payroll=Tk()
payroll.geometry("1350x650+0+0")
payroll.title("PAYROLL MANAGEMENT SYSTEM")

def Exit():
    payroll.destroy()
########################################
#def ShowData():
    #("yahi nhi bann rha hai mera")
######################################
def Reset():
    Name.set(" ")
    Address.set(" ")
    City.set(" ")
    PinCode.set(" ")
    Salary.set(" ")
    DA.set(" ")
    Overtime.set(" ")
    Pension.set(" ")
    PayDate.set(" ")
    Code.set(" ")
    Shift.set(" ")
    DeductedSalary.set(" ")
    WorkExperience.set(" ")
    BloodGroup.set(" ")
    Gender.set(" ")
    MobileNumber.set(" ")
    Post.set(" ")
    dept.set(" ")
    age.set(" ") 
    Email.set(" ")

Name =StringVar()
Address =StringVar()
City =StringVar()
PinCode =StringVar()
Salary =StringVar()
DA =StringVar()
Overtime =StringVar()
Pension =StringVar()
PayDate =StringVar()
Code =StringVar()
Shift =StringVar()
DeductedSalary =StringVar()
WorkExperience =StringVar()
BloodGroup =StringVar()
Gender =StringVar()
MobileNumber =StringVar()
Post =StringVar()
dept =StringVar()
age =StringVar() 
Email =StringVar()

tops=Frame(payroll,width=1350,height=00,bd=16, relief="raise",bg="red")
tops.pack(side=TOP)
LF=Frame(payroll,width=500, height=200,bd=16,bg="orange", relief="raise")
LF.pack(side=LEFT)
RF=Frame(payroll,width=500, height=200,bd=16,bg="orange", relief="raise")
RF.pack(side=RIGHT)

lblInfo=Label(tops, font=("arial",50,"bold"),text="KAILASH PHARMACY",fg='Steel Blue',bd=10)
lblInfo.grid(row=0,column=0)

LeftInsideLF=Frame(LF,width=200, height=200, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF,width=250, height=200, relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF,width=250, height=200, relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF,width=200, height=200, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF,width=250, height=200, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF,width=250, height=200, relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#------------------------------------------------left side-----------------------------------------------------------
lblName=Label(LeftInsideLF, font=("arial",16,"bold"),text="Name",fg='steel blue',bd=10,anchor='w')
lblName.grid(row=0,column=0)
txtName=Entry(LeftInsideLF, font=("arial",12,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=Name)
txtName.grid(row=0,column=1)
lblAddress=Label(LeftInsideLF, font=("arial",16,"bold"),text="Address",fg='steel blue',bd=10,anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress=Entry(LeftInsideLF, font=("arial",12,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=Address)
txtAddress.grid(row=1,column=1)
lblCity=Label(LeftInsideLF, font=("arial",16,"bold"),text="City",fg='steel blue',bd=10,anchor='w')
lblCity.grid(row=2,column=0)
txtCity=Entry(LeftInsideLF, font=("arial",12,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=City)
txtCity.grid(row=2,column=1)
lblPinCode=Label(LeftInsideLF, font=("arial",16,"bold"),text="Pin Code",fg='steel blue',bd=10,anchor='w')
lblPinCode.grid(row=3,column=0)
txtPinCode=Entry(LeftInsideLF, font=("arial",12,"italic"),bd=10, width=65,bg="powder blue",justify='left',textvariable=PinCode)
txtPinCode.grid(row=3,column=1)

#---------------------------------------------left inside left--------------------------------------------------------


lblSalary=Label(LeftInsideLFLF, font=("arial",16,"bold"),text="Salary",fg='steel blue',bd=10,anchor='w')
lblSalary.grid(row=0,column=0)
txtSalary=Entry(LeftInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Salary)
txtSalary.grid(row=0,column=1)
lblDA=Label(LeftInsideLFLF, font=("arial",16,"bold"),text="DA",fg='steel blue',bd=10,anchor='w')
lblDA.grid(row=1,column=0)
txtDA=Entry(LeftInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=DA)
txtDA.grid(row=1,column=1)
lblOverTime=Label(LeftInsideLFLF, font=("arial",16,"bold"),text="Over Time",fg='steel blue',bd=10,anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime=Entry(LeftInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Overtime)
txtOverTime.grid(row=2,column=1)
lblPension=Label(LeftInsideLFLF, font=("arial",16,"bold"),text="Pension",fg='steel blue',bd=10,anchor='w')
lblPension.grid(row=3,column=0)
txtPension=Entry(LeftInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Pension)
txtPension.grid(row=3,column=1)

lblPayDate=Label(LeftInsideRFRF, font=("arial",16,"bold"),text="Pay Date",fg='steel blue',bd=10,anchor='w')
lblPayDate.grid(row=0,column=0)
txtPayDate=Entry(LeftInsideRFRF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=PayDate)
txtPayDate.grid(row=0,column=1)
lblCode=Label(LeftInsideRFRF, font=("arial",16,"bold"),text="Job Code",fg='steel blue',bd=10,anchor='w')
lblCode.grid(row=1,column=0)
txtCode=Entry(LeftInsideRFRF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Code)
txtCode.grid(row=1,column=1)
lblShift=Label(LeftInsideRFRF, font=("arial",16,"bold"),text="Shift",fg='steel blue',bd=10,anchor='w')
lblShift.grid(row=2,column=0)
txtShift=Entry(LeftInsideRFRF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Shift)
txtShift.grid(row=2,column=1)
lblDeductedSalary=Label(LeftInsideRFRF, font=("arial",16,"bold"),text="Deducted Salary",fg='steel blue',bd=10,anchor='w')
lblDeductedSalary.grid(row=3,column=0)
txtDeductedSalary=Entry(LeftInsideRFRF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=DeductedSalary)
txtDeductedSalary.grid(row=3,column=1)

#------------------------------------------------right side-----------------------------------------------------------
lblWorkExperience=Label(RightInsideLF, font=("arial",16,"bold"),text="Work Exp.",fg='steel blue',bd=10,anchor='w')
lblWorkExperience.grid(row=0,column=0)
txtWorkExperience=Entry(RightInsideLF, font=("arial",13,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=WorkExperience)
txtWorkExperience.grid(row=0,column=1)
lblBloodGroup=Label(RightInsideLF, font=("arial",16,"bold"),text="Blood Grp.",fg='steel blue',bd=10,anchor='w')
lblBloodGroup.grid(row=1,column=0)
txtBloodGroup =Entry(RightInsideLF, font=("arial",13,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=BloodGroup)
txtBloodGroup .grid(row=1,column=1)
lblGender=Label(RightInsideLF, font=("arial",16,"bold"),text="Gender",fg='steel blue',bd=10,anchor='w')
lblGender.grid(row=2,column=0)
txtGender =Entry(RightInsideLF, font=("arial",13,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=Gender)
txtGender.grid(row=2,column=1)
lblMobileNumber=Label(RightInsideLF, font=("arial",16,"bold"),text="Mobile No.",fg='steel blue',bd=10,anchor='w')
lblMobileNumber.grid(row=3,column=0)
txtMobileNumber=Entry(RightInsideLF, font=("arial",13,"italic"),bd=10,width=65,bg="powder blue",justify='left',textvariable=MobileNumber)
txtMobileNumber.grid(row=3,column=1)

#----------------------------------INSIDE RIGHT SIDE---------------------------------------------------------------

lblPost=Label(RightInsideLFLF, font=("arial",16,"bold"),text="Post",fg='steel blue',bd=10,anchor='w')
lblPost.grid(row=0,column=0)
txtPost=Entry(RightInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Post)
txtPost.grid(row=0,column=1)
lbldept=Label(RightInsideLFLF, font=("arial",16,"bold"),text="Department",fg='steel blue',bd=10,anchor='w')
lbldept.grid(row=1,column=0)
txtdept=Entry(RightInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=dept)
txtdept.grid(row=1,column=1)
lblage=Label(RightInsideLFLF, font=("arial",16,"bold"),text="Age",fg='steel blue',bd=10,anchor='w')
lblage.grid(row=2,column=0)
txtage=Entry(RightInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=age)
txtage.grid(row=2,column=1)
lblEmail=Label(RightInsideLFLF, font=("arial",16,"bold"),text="Email Address",fg='steel blue',bd=10,anchor='w')
lblEmail.grid(row=3,column=0)
txtEmail=Entry(RightInsideLFLF, font=("arial",12,"italic"),bd=10,insertwidth=8,bg="powder blue",justify='left',textvariable=Email)
txtEmail.grid(row=3,column=1)

#--------------------------------------------------------------------------------------------------------------
ResetData=Button(RightInsideRFRF,padx=8,bd=8,fg="black",font=("arial",16,"bold"),width=10,text="Reset Data",bg="powder blue",relief="raise",command=Reset).grid(row=1,column=0)
code=Button(RightInsideRFRF,padx=8,bd=8,fg="black",font=("arial",16,"bold"),width=10,text="Show Data",bg="powder blue",relief="raise").grid(row=3,column=0)
logout=Button(RightInsideRFRF,padx=8,bd=8,fg="black",font=("arial",16,"bold"),width=10,text="Exit",bg="powder blue",relief="raise",command=Exit).grid(row=4,column=0)

payroll.mainloop()

