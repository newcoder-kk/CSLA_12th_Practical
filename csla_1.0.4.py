#computer lab assistant program version 1.0.1
#options undertaken 1)entry of the student details
#                   2)display of student details in tablular format
#                   3)search option for student record
import os,sys
import pickle
import datetime
import time
from tkinter import *

def Timer(t=305):
    choice="f"
    global decis
    decis=100
    global t

    while t and choice!="e" or choice!="E": 
        mins,secs=divmod(t,60) 
        timer='{:02d}:{:02d}'.format(mins,secs) 
        time.sleep(1) 
        t-=1
        if t==300:
            root=Tk()
            messagebox.showwarning("TIMER ALERT","Time remaining/n 5 mins")
            root.destroy()
        elif t==120:
            messagebox.showwarning("TIMER ALERT","Time remaining/n 2 mins")
        elif t==60:
            messagebox.showwarning("TIMER ALERT","Time remaining/n 1 min")
        choice=input("Enter E or e when you are ready to leave:")           #################
    else:
        decis=101
        return decis

def Exit():
    while True:
        print("Hello student would you like to end this session now?")
        print('''Type 'y' for yes
Type 'n' for no ''')
        et=''
        en=input("Enter your choice here:")
    
        if en=="Y" or en=="y":
            et=str(datetime.datetime.now()).split()
            et=et[1]
            et=et[0:8]
            print("Your time of leaving is",et)
            print()
            print("Hope you enjoyed your lab session")
            print("Have a GREAT DAY AHEAD")
            
            return et
        
        elif en=="n" or en=="N":
            print("Please continue your session")
            print()

        else:
            print("Invalid choice!!, please re-enter your choice")
            print()

def deldup(adm,date,time):
    f=open("student details(1.0.3).dat",'rb')
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("student details(1.0.3).dat","w")
    f.close()
    f=open("student details(1.0.3).dat","ab")
    fgg1=1
    for rec in reclst:
        if rec["adm no."]==adm and rec["Date"]==date and rec["Time in"]==time and rec["Time out"]==None and fgg1==1:
            fgg1=2
            continue
        else:
            pickle.dump(rec,f)
            
def entry1():
    print()
    print("You have chosen to start a session")
    print("Please enter the following details to start your session")
    print()
    admno=int(input("Enter your admission number:-"))
    name=input("Enter the name of student:")
    name=name.title()
    class_c=input("Enter your class in format(ex:-12):-")
    class_s=input('Enter your section in (A,B,C):-')
    class_=str(class_c+"-"+class_s)
    
    s=str(datetime.datetime.now())
    s=s.split()
    s1=s[0]
    s2=s[1]
    s2=s2[0:8]
    s3=None
    print()
    print("Hello",name,"Your time of entry is:",s2)
    d1={"Name":name,"Class":class_,"adm no.":admno,"Time in":s2,"Time out":s3,"Date":s1}
    f=open("student details(1.0.3).dat",'ab')
    pickle.dump(d1,f)
    f.flush()
    print('''Your entry record has been saved
now you can minimise this tab and continue with your work''')

    while decis!=101:
        Timer()
    
    while decis==101:
        print('''Your student session has expired!!!
    1)Press 1 to extent your session
    2)Press 2 to end your session''')
        while True:
            i1=int(input("Enter your choice here"))
            if i1==2:
                s3=Exit()
                d1["Time out"]=s3
                pickle.dump(d1,f)
                f.close()
                break
            elif i1==1:
                exttime=int(input("Enter the extra time in minutes"))
                Timer(exttime*60)
                break
            else:
                print("INVALID CHOICE,please re-enter your choice or continue with your session")

    deldup(admno,s1,s2)
    print()
    print()
    print()

def GREET():
    s=str(datetime.datetime.now())
    sm=int(s[11:13])
    if sm<=12:
        return "GOOD MORNING"
    elif sm>=12 and sm<=17:
        return "GOOD AFTERNOON"
    else:
        return "GOOD EVENING"

def show_all_entry():
    print()
    print()
    print("You have chosen to show all record")
    print()
    
    f=open("student details(1.0.3).dat","rb")
    cnt=1
    a1=b1=""
    for i in range(91):
        a1+="_"
    print(a1)
    for k in range(91):
        b1+="-"
    print("| Sno. | Name of student         | Class | Adm no. |  Time in   |  Time out  |   Date     |")
    print(b1)

    while True:
        try:
            d1=pickle.load(f)
            [c1,d21,e1,f1,g1,h1,j1]=[cnt,d1["Name"],d1["Class"],d1["adm no."],d1["Time in"],d1["Time out"],d1["Date"]]
            c1=str(c1)
            nd1=23-len(d21)
            spc1=spc2=spc3=""
            for d_1 in range(nd1):
                spc1+=" "
            sp1=spc1
            for d_2 in range(4-len(e1)):
                spc2+=" "
            sp2=spc2
            for d_3 in range(3-len(c1)):
                spc3+=" "
            sp3=spc3
            d21=d21+sp1
            c1=" "+c1+sp3
            e1=" "+e1+sp2
            f1=" "+str(f1)+"  "
            g1=" "+g1+" "
            if h1==None:
                h1="------- "
            else:
                h1=h1
            h1=" "+h1+" "
            print("|",c1,"|",d21,"|",e1,"|",f1,"|",g1,"|",h1,"|",j1,"|")
            print(b1)

        except EOFError:
            break
        cnt=cnt+1
    f.close()
    print()
    print()
    print()

def search_entry(adno):
    f=open("student details(1.0.3).dat",'rb')
    flag=1
    while True:
        try:
            d1=pickle.load(f)
            if adno==d1["adm no."]:
                print("Record found!!")
                print("   student name:",d1["Name"])
                print("   class       :",d1["Class"])
                print("   Time in     :",d1["Time in"])
                print("   Time out    :",d1["Time out"])
                print()
                print()
                print()
                flag=0


        except EOFError:
            break

    if flag==1:
        print("SORRY NO RECORD WAS FOUND!!")
        print()
        print()
        print()


def delete_rec():
    amd=int(input("Enter the 4 digit admission no. :-"))
    f=open("student details(1.0.3).dat",'rb')
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("student details(1.0.3).dat","w")
    f.close()
    f=open("student details(1.0.3).dat","ab")
    fgg1=1
    for rec in reclst:
        if rec["adm no."]==amd and fgg1==1:
            fgg1=2
            continue
        else:
            pickle.dump(rec,f)

    if fgg1==1:
        print("SORRY NO RRECORD WAS FOUND TO DELETE!!!")
        print()
        print()
        print()
    else:
        print("RECORD DELETED!!!")
        print()
        print()
        print()
    f.close()


#TRUE PROGRAM

    
while True:
    print("Enter 1 for STUDENT ACCESS:")
    print("Enter 2 for MASTER ACCESS:")
    print("Enter 3 to quit the program:")
    i=input("Enter your choice:-")
    i=int(i)

    if i==1:
        print()
        print()
        print(GREET()+" Student")
        print("Enter 1 to start a session:")
        f=int(input("Enter Your choice here:"))
        if f==1:
            entry1()
        else:
            print("Enter Invalid Choice!!!Please Re-enter your choice")
            

    elif i==2:
        for b in range(0,3):
            p=int(input("Please enter 5-digit password:-"))
            if p==12345:
                flag_21=True 
                break
            else:
                print("incorrect password!! Try again ")
                print("Trials Remaining:",2-b) 
        else:
            print("PASSWORD INCORRECT!!")
            sys.exit(0)

        if flag_21==True:
            while True:
                print()
                print()
                print(GREET()+" Sir")
                print("Enter 1 to show all student records;")
                print("Enter 2 to search student record by admission number:")
                print("Enter 3 to delete student record by admission number:")
                print("Enter 4 to quit the Master access session")
                m=int(input("Enter your choice here:"))

                if m==1:
                    show_all_entry()
                elif m==2:
                    amd=int(input("Enter the 4 digit admission no. :-"))
                    search_entry(amd)
                elif m==3:
                    delete_rec()
                elif m==4:
                    print()
                    print()
                    break
                else:
                    print("Invalid choice!!!!Please re-enter the choice")
                
            
    elif i==3:
        print()
        print()
        print("Thank you for using CSLA!!")
        sys.exit(0)

    else:
        print("Invalid choice,kindly re-enter your choice")

        
