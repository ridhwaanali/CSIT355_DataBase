#ridhwaan ali
import sqlite3
from sqlite3 import Error
import sys
import re
finalproject_db=r"/Users/ridhwaanali/Desktop/355proj/finalproject.db"
conn = sqlite3.connect(finalproject_db)
c = conn.cursor()

def mycourse():

    def enrollcourse():
        enrollcourse=mycourse(enrollcourse)

    def removecourse():
        removecourse=mycourse(enrollcourse)
 
    
def create_connection(finalproject_db):
    global c
    global conn

    conn = None
    try:
        conn = sqlite3.connect(finalproject_db)
    except Error as e:
        print(e)
    return conn

def main():
    database = r"/Users/ridhwaanali/Desktop/355proj/finalproject.db"
    conn = create_connection(database)
    
def login():
    print("Enter your student id : ")
    loginid=input()
    print("Welcome")


def menu():   
    print("MAIN MENU")
    print()
    choice = input("""
                      L: List of all classes
                      E: Enroll 
                      W: Withdraw
                      S: Search
                      M: MyClasses
                      X: Exit

                      Please enter your choice: """)
#Choice L
    if choice == "L" or choice =="l":
        global c
        print("List of classes")
        for row in c.execute("SELECT * FROM courses"):
            print(row)


        anykey=input("press any key to return to main menu")
        menu()

#Choice E
    elif choice == "E" or choice =="e":
        enrollchoice=input("would you like to enroll or view courses enrolled?")
        if enrollchoice=="enroll" or enrollchoice=="Enroll":
            enrollcourse=input("please choose a class you wish to enroll in")
            print("you have been registered")
        elif enrollchoice=="view" or enrollchoice=="View":
                print("List of Enrolled Classes")
                for row in c.execute("SELECT * FROM courses"):
                    print (row)
                for row in c.execute("SELECT * FROM enrollment"):
                    print (row)

        anykey=input("press any key to return to main menu")
        menu()
#Choice W        
    elif choice == "W" or choice =="w":
            purgechoice=input("would you like to remove the last class you enrolled in y/n?")
            if purgechoice == "Y" or purgechoice=="y":
                removecourse.pop(0)
            elif purgechoice == "N" or purgechoice=="n":
                print("no courses removed")

            anykey=input("press any key to return to main menu")
            menu()            
#Choice S
    elif choice=="S" or choice=="s":
        pattern="Calc1 Chem Bio Phys Hist"
        string= "Calc1 Chem Bio Phys Hist"
        re.search(pattern,string)
        patterns=input("Please search a course you are looking for")
        if patterns==pattern:
            print (re.search(pattern,string))
        else:
            print("sorry your search was invalid")

        anykey=input("press any key to return to main menu")
        menu()                
    
#Choice M
    elif choice =="M" or choice=="m":
            print("Your current enrolled classes", mycourse())
            
            
            anykey=input("press any key to return to main menu")
            menu()        


#Choice X        

    elif choice=="X" or choice=="x":
        print("sucessfully logout")
        sys.exit

#Wrong Choice
    else:
        print("You must only select letters listed above.")
        print("Please try again")

    anykey=input("press any key to return to main menu")
    menu()

conn.commit()
main()
login()
menu()



        
        


