import sys #this allows you to use the sys.exit command to quit/logout of the application
import glob
import os
import requests

##resp = requests.get("http://localhost:5000/files/")
##if resp.status_code != 200:
##    # This means something went wrong.
##    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
##for todo_item in resp.json():
##    print('{} {}'.format(todo_item['id'], todo_item['summary']))

def _url(path):
        return "http://localhost:5000" + path

def download_file(filename):
        response = requests.get(_url('/files/{}'.format(filename)))
        with open(filename, 'w+') as f:
            f.write(response.text)
            f.close()
        return response

def upload_file(filename):
        #check if file exists
        #If ok do open(file)
        #If not ok return bad status
        with open(filename, 'r') as f:
            upload_data = f.read()
            f.close()
            return requests.put(_url('/files/{}'.format(filename)),
                                data=upload_data
                                )

def list_files():
        response = requests.get(_url('/files'))
        return response

def delete_file(filename):
        return requests.delete(_url('/files/{}'.format(filename)))

def print_menu():
    print()
    print("************MAIN MENU**************")
    menu_text = """
        1: List all files
        2: Add a file
        3: Download a file
        4: Delete a file
        Q: Quit

        """
    print(menu_text)

def main():
    print_menu()
    status = 0
    while (status == 0):
        status = menu()

def menu():
    choice = input("Please enter your choice: ")

    if choice == "1":
        resp = list_files()
        print()
        print("**files on server**")
        files = resp.json()
        for file in files:
            print(file)
        if resp.status_code != 200:
                print("Could not execute your request")
        return 0
    elif choice == "2":
        filename = input("Please enter filename: ")
        resp = upload_file(filename)
        print(resp)
        return 0
        
    elif choice == "3":
        filename = input("Please enter filename: ")
        download_file(filename)
        return 0
    elif choice == "4":
        filename = input("Please enter filename: ")
        delete_file(filename)
        return 0
    elif choice=="Q" or choice=="q":
        return 1
    elif choice=="H" or choice=="h":
        print_menu()
        return 0
    else:
        print("You can only select 1, 2, 3, 4 or Q")
        print("Please try again")
        return 0

        

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

if __name__== "__main__":
  main()
