import sys #this allows you to use the sys.exit command to quit/logout of the application
import glob
import os
import requests
import server
from server import list_files, add_file, get_file, delete_file


def main():

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
        server.list_files()
    elif choice == "2":
        server.add_file()
    elif choice == "3":
        server.get_file()
    elif choice == "4":
        server.delete_file()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You can only select 1, 2, 3, 4 or Q")
        print("Please try again")
        menu()

##def enterfilename():
##    # asks user for filename
##    filename = input("Insert 'filename.txt' >>> ")
##    # opens user inputted filename ".txt" and (w+) creates new file if it dont already exists
##    with open(filename, 'w+') as f:
##        f.close()
##        print("File created")
##        menu()
##
##
##def listfiles():
##    myFiles = glob.glob('*.txt')
##    print(myFiles)
##    print()
##
##    pass        
##    menu()
##        
##
##def downloadfile():
##    myFiles = glob.glob('*.txt')
##    print(myFiles)
##    print()
##    filename = input("Enter name of file you want to download: >>> ")
##      # checking whether file exists or not
##    if  os.path.exists(filename):
##        f=open(filename, 'w+')
##        f.close()
##        print("File downloaded")
##    else:
##    # file not found message
##        print("File not found in the directory")
##    pass
##    
##
##
##
##def deletefile():
##    myFiles = glob.glob('*.txt')
##    print()
##   # print("Enter name of file you want to delete")
##    print(myFiles)
##    filename = input("Enter name of file you want to delete: ")
##    # checking whether file exists or not
##    if  os.path.exists(filename):
##        os.remove(filename)
##        print("File deleted")
##    else:
##    # file not found message
##        print("File not found in the directory")
##    
##    menu()    
##    
##
##menu()

main()
