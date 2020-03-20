import sys #this allows you to use the sys.exit command to quit/logout of the application
import glob
import os
import requests

def main():
##    login()
##    
##def login():
##    username="kjell"
##    password="master"
##    print("Enter username : ")
##    answer1=input()
##    print("Enter password : ")
##    answer2=input()
##    if answer1==username and answer2==password:
##        print("Welcome - Access Granted")
        menu()

def menu():
    print()
    print("************MAIN MENU**************")


    choice = input("""
        1: List all files
        2: Add a file
        3: Download a file
        4: Delete a file
        Q: Quit

        Please enter your choice: """)

    if choice == "1":
        listfiles()
    elif choice == "2":
        enterfilename()
    elif choice == "3":
        downloadfile()
    elif choice == "4":
        deletefile()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You can only select 1, 2, 3, 4 or Q")
        print("Please try again")
        menu()

def enterfilename():
    # asks user for filename
    filename = input("Insert 'filename.txt' >>> ")
    # opens user inputted filename ".txt" and (w+) creates new file if it dont already exists
    with open(filename, 'w+') as f:
        f.close()
        print("File created")

##    http.request(
##    'POST',
##    'localhost:5000',
##    )
        menu()


def listfiles():
    myFiles = glob.glob('*.txt')
    print(myFiles)
    print()
##    response = requests.get('localhost:5000')
##    print(response)
    pass        
    menu()
        

def downloadfile():
    myFiles = glob.glob('*.txt')
    print(myFiles)
    print()
    filename = input("Enter name of file you want to download: >>> ")
      # checking whether file exists or not
    if  os.path.exists(filename):
        f=open(filename, 'w+')
        f.close()
        print("File downloaded")
    else:
    # file not found message
        print("File not found in the directory")
    pass
    



def deletefile():
    myFiles = glob.glob('*.txt')
    print()
   # print("Enter name of file you want to delete")
    print(myFiles)
    filename = input("Enter name of file you want to delete: ")
    # checking whether file exists or not
    if  os.path.exists(filename):
        os.remove(filename)
        print("File deleted")
    else:
    # file not found message
        print("File not found in the directory")
    
    menu()    
    

menu()

main()
