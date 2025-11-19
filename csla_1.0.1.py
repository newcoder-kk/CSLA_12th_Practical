#computer lab assistant program version 1.0.1
#options undertaken 1)entry of the student details
#                   2)display of student details
#                   3)search option for student record
import os,sys
import pickle
import csv

def entry1():
    name=input("Enter the name of student:")
    class_=input("Enter ur class in format(ex:- 12-A)")
    admno=int(input("Enter your admission number"))
    time_in=input("Enter time in HH:MM(24 hours format)")
    time_out=input("Enter time out HH:MM(24 hours format)")
    d1={"Name":name,"Class":class_,"adm no.":admno,"Time in":time_in,"Time out":time_out}

    f=open("student details.dat",'ab')
    pickle.dump(d1,f)
    f.close()


def show_all_entry():
    f=open("student details.dat","rb")
    cnt=1
    while True:
        try:
            d1=pickle.load(f)
            print("Record number {}:".format(cnt))
            print("   Student name    :",d1["Name"])
            print("   Class           :",d1["Class"])
            print("   Admission number:",d1["adm no."])
            print("   Time in         :",d1["Time in"])
            print("   Time out        :",d1["Time out"])
            print()
        except EOFError:
            break
        cnt+=1
    f.close()


def search_entry(adno):
    f=open("student details.dat",'rb')
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


while True:
    print("Enter 1 to enter student record:")
    print("Enter 2 to view all student record:")
    print("Enter 3 to search student record by admission number:")
    print("Enter 4 to quit the program")
    i=int(input("enter your choice:-"))

    if i==1:
        entry1()
        print("Your entry has been saved")
        print()

    elif i==2:
        for b in range(0,3):
            p=int(input("Plese enter 5-digit password"))
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
            p=int(input("Plese enter 5-digit password"))
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
        print("Thank you for using CSLA!!")
        sys.exit(0)

    else:
        print("invalid choice,re-enter your choice")

        
