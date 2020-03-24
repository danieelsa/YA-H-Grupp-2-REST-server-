import sys  # this allows you to use the sys.exit command to quit/logout of the application
import glob
import requests
from pathlib import Path
import os

LOCAL_DIRECTORY = Path(__file__).parent.parent / "files"

def _url(path):
    return "http://localhost:5000" + path


def download_file(filename):
    response = requests.get(_url('/files/{}'.format(filename)))
    #print(response.status_code)
    if response.status_code != 200:
        return response.status_code
    with open(LOCAL_DIRECTORY / filename, 'w+') as f:
        f.write(response.text)
        f.close()
    return response.status_code


def upload_file(filename):
    file_path = LOCAL_DIRECTORY / filename
    status=0


    with open(file_path, 'w+') as f:
        upload_data = f.read()
        f.close()
        
        status=requests.put(_url('/files/{}'.format(filename)),
                            data=upload_data
                            ).status_code
    if status==201:
        os.remove(file_path)
    return status

def list_files():
    response = requests.get(_url('/files'))
    if response.status_code != 200:
        print("Could not execute your request")
        return response.status_code

    print()
    print("** Files on server **")
    files = response.json()
    for file in files:
        print("   " + file)
    return response.status_code


def delete_file(filename):
    return requests.delete(_url('/files/{}'.format(filename))).status_code


def print_menu():
    print()
    print("************MAIN MENU**************")
    menu_text = """
        1: List all files
        2: Add a file
        3: Download a file
        4: Delete a file
        H: Print menu
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
        list_files()
        return 0

    elif choice == "2":
        filename = input("Please enter filename.txt: ")
        resp = upload_file(filename)

        if resp == 201:
            print("File uploaded!")
        elif resp == 0:
            print("Could not find file!")
        else:
            print("Failed to upload file!")
        return 0

    elif choice == "3":
        filename = input("Please enter filename: ")
        resp = download_file(filename)

        if resp == 200:
            print("File downloaded!")
        else:
            print("Failed to find file on server!")
        return 0

    elif choice == "4":
        filename = input("Please enter filename: ")
        resp = delete_file(filename)

        if resp == 200:
            print("File deleted!")

        elif resp == 404:
            print("Could not find file!")

        else:
            print("Unknown response!")
        return 0

    elif choice == "Q" or choice == "q":
        return 1

    elif choice == "H" or choice == "h":
        print_menu()
        return 0
    else:
        print("You can only select 1, 2, 3, 4 or Q")
        print("Please try again")
        return 0

if __name__ == "__main__":
    main()
