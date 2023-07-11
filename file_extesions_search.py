import os
import os.path

from tkinter import Tk
from tkinter import filedialog

def get_files(extensions:list, root_directory:str, search_sub_directories:bool):
    filepaths = []
    if search_sub_directories == True:
        for root, dirs, files in os.walk(root_directory):
            for filename in files:
                if os.path.splitext(filename)[1] in extensions:
                    filepaths.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(root_directory):
            if os.path.splitext(filename)[1] in extensions:
                filepaths.append(os.path.join(root_directory, filename))
    return filepaths
    

def extension_menu():
    print('\nType \'0\' if you want to exit this program')
    print('Type an extension you want to search for (\'done\' if you are done): ')

def boolean_menu():
    print('Would you like to search sub directories as well?')
    print('\'True\' for yes, \'False\' for no (case sensitive) ')

def main():
    extensions = []

    while True:
        try:
            extension_menu()
            find_extension = input()
            if find_extension.casefold() == 'done':
                break
            elif find_extension.isdigit() and find_extension != '0':
                print('Error, strings only\n')
            elif find_extension == '0':
                print('Exiting program')
                exit()
            else:
                extensions.append(find_extension)
        
        except Exception as e:
            print('Error\n')

    while True:
        try:
            boolean_menu()
            search_sub = input()
            if search_sub == 'True' or search_sub == 'False':
                search_sub = eval(search_sub)
                break
            else:
                print('Error, try again\n')

        except Exception as e:
            print('Error\n')

    root = Tk()
    root.withdraw()
    
    print("Please select the root directory")
    root_dir = filedialog.askdirectory()

    print(get_files(extensions, root_dir, search_sub))

if __name__ == "__main__":
    main()