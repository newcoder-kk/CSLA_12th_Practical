#computer lab assistant program version 1.0.1
#options undertaken 1)entry of the student details
#                   2)display of student details in tablular format
#                   3)search option for student record
import os,sys
import pickle
import csv

def entry1():
    name=input("Enter the name of student:")
    class_=input("Enter ur class in format(ex:- 12-A):-")
    admno=int(input("Enter your admission number:-"))
    time_in=input("Enter time in HH:MM(24 hours format):-")
    time_out=input("Enter time out HH:MM(24 hours format):-")
    date=input("Enter date of entry(DD/MM/YYYY):-")
    d1={"Name":name,"Class":class_,"adm no.":admno,"Time in":time_in,"Time out":time_out,"Date":date}

    f=open("student details(1.0.2).dat",'ab')
    pickle.dump(d1,f)
    f.close()


def show_all_entry():
    f=open("student details(1.0.2).dat","rb")
    cnt=1
    a1=b1=""
    for i in range(86):
        a1+="_"
    print(a1)
    for k in range(86):
        b1+="-"
    print("| Sno. | Name of student         | Class | Adm no. | Time in | Time out |   Date     |")
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
            h1=" "+h1+"  "
            print("|",c1,"|",d21,"|",e1,"|",f1,"|",g1,"|",h1,"|",j1,"|")
            print(b1)

        except EOFError:
            break
        cnt=cnt+1
    f.close()


def search_entry(adno):
    f=open("student details(1.0.2).dat",'rb')
    flag=1
    while True:
        try:
            d1=pickle.load(f)
            if adno==d1["adm no."]:
                print("record found!!")
                print("   student name:",d1["Name"])
                print("   class       :",d1["Class"])
                print("   Time in     :",d1["Time in"])
                print("   Time out    :",d1["Time out"])
                print()
                flag=0


        except EOFError:
            break

    if flag==1:
        print("sorry no record was found!!")


def delete_rec(admn):
    f=open("student details(1.0.2).dat",'wb+')
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    fgg1=1
    for x in reclst:
        if x["adm no."]==admn:
            fgg1=2
            continue
        pickle.dump(x,f)

    if fgg1==1:
        print("sorry no record found to delete")
    else:
        print("record deleted")
    f.close()
        
while True:
    print("Enter 1 to enter student record:")
    print("Enter 2 to view all student record:")
    print("Enter 3 to search student record by admission number:")
    print("Enter 4 to delete student record by admission number:")
    print("Enter 5 to quit the program")
    i=int(input("Enter your choice:-"))

    if i==1:
        entry1()
        print("Your entry has been saved")
        print()

    elif i==2:
        for b in range(0,3):
            p=int(input("Please enter 5-digit password:-"))
            if p==12345:
                show_all_entry()
                print()
                print()
                break
            else:
                print("incorrect password!! Try again")

        else:
            print("password incorrect!!")
            sys.exit(0)

    elif i==3:
        for b in range(0,3):
            p=int(input("Please enter 5-digit password:-"))
            if p==12345:
                amd=int(input("Enter the 4 digit admission no. :-"))
                search_entry(amd)
                print()
                break
            else:
                print("incorrect password!! Try again")

        else:
            print("password incorrect!!")
            sys.exit(0)

    elif i==4:
        for b in range(0,3):
            p1=int(input("Please enter 5-digit password:-"))
            if p1==12345:
                amd=int(input("Enter the 4 digit admission no. :-"))
                delete_rec(amd)
                print()
                break
            else:
                print("incorrect password!! Try again")

        else:
            print("password incorrect!!")
            sys.exit(0)

    elif i==5:
        print()
        print("Thank you for using CSLA!!")
        sys.exit(0)

    else:
        print("invalid choice,kindly re-enter your choice")

        
