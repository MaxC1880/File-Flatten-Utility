'''
This is a program that acts as a file directory utility. You can either flatten an entire system of files into one single directory of files using a dictionary to store the paths,
and you can do the reverse and unflatten a single directory into a system of files.
'''
import os
import os.path
import shutil

from tkinter import Tk
from tkinter import filedialog


def flatten_intoOneDir(root_dir, output_dir, action_choice, delete_choice):
    DirDict = {}
    count = 65

    for root, dirs, files in os.walk(root_dir):
        og_dir = root.replace(root_dir, '')
        DirDict[og_dir] = chr(count)
        count += 1
        letter_append = DirDict[og_dir]
        

        for filename in files:
            old_file = os.path.join(root, filename)
            new_file = os.path.join(output_dir, letter_append + filename)

            while True:
                try:
                    if delete_choice == 1:
                        shutil.move(old_file, new_file)
                        break
                    elif delete_choice == 2:
                        shutil.copy(old_file, new_file)
                        break
                    
                except(Exception):
                    print("Something went wrong with the file, try again\n")
                    file_actions(action_choice, delete_choice)

    with open(output_dir + '/DICTIONARY.txt', 'w') as f:
        for k, v in DirDict.items():
            f.write(str(v) + str(k) + '\n')

        f.close()

def expand_intoSubDir(root_dir, destination_dir, action_choice, delete_choice):
    DirDict = {}

    for file in os.listdir(root_dir):
        if file == 'DICTIONARY.txt':
            file_name = os.path.join(root_dir, 'DICTIONARY.txt')
            with open(file_name, 'r') as f:
                for line in f.readlines():
                    letter = line[0]
                    DirDict[letter] = line[1:].replace('\n', '')

    for file in os.listdir(root_dir):
        if file == 'DICTIONARY.txt':
            continue
        else:
            if os.path.isfile(os.path.join(root_dir, file)):
                source_filepath = os.path.join(root_dir, file)
                file_char = file[0]
                og_filepath = DirDict[file_char]
                destination_directory = destination_dir
                og_filepath = og_filepath.split('\\')

                for components in og_filepath:
                    destination_directory = os.path.join(destination_directory, components)
                    os.makedirs(destination_directory, exist_ok = True)

                destination_filepath = os.path.join(destination_directory, file[1:])
                
                while True:
                    try:
                        if delete_choice == 1:
                            shutil.move(source_filepath, destination_filepath)
                            break
                        elif delete_choice == 2:
                            shutil.copy(source_filepath, destination_filepath)
                            break

                    except(Exception):
                        print("Something went wrong with the file, try again\n")
                        file_actions(action_choice, delete_choice)
                        
def print_menu():
    print("Please select an option:")
    print("0: Exit program")
    print("1: Collapse directory to flat files")
    print("2: Uncollapse flat files to directory")

def delete_menu():
    print("Would you like to delete the original files once they are copied over: ")
    print("0: Exit program")
    print("1: Yes")
    print("2: No")


def file_actions(action_choice, delete_choice):
    root = Tk()
    root.withdraw()

    print("Please select the root directory")
    root_directory = filedialog.askdirectory()
    print("Please select the output directory")
    output_directory = filedialog.askdirectory()

    if output_directory == root_directory:
        print( '\nError, output directory cannot be the same as the root directory, try again\n')
    else:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
                
        if action_choice == 1:
            flatten_intoOneDir(root_directory, output_directory, action_choice, delete_choice)
        elif action_choice == 2:
            expand_intoSubDir(root_directory, output_directory, action_choice, delete_choice)
        
        if delete_choice == 1:
            shutil.rmtree(root_directory)
            print('\nYour files have been copied over and the original directory has been deleted')
        elif delete_choice == 2:
            print('\nYour files have been copied over and the original directory is still intact ')

def main():
    while True:
        try:
            print_menu()
            action_choice = int(input())

            if action_choice == 0:
                print("Program has been exited")
                exit()
            elif action_choice == 1 or action_choice == 2:
                delete_menu()
                delete_choice = int(input())

                if delete_choice == 0:
                    print("Program has been exited")
                    exit()
                elif delete_choice == 1 or delete_choice == 2:
                    file_actions(action_choice, delete_choice)
                    break
                else:
                    print('\nIncorrect value for delete choice, retry\n')
            else:
                print('\nIncorrect value for action choice, try again\n')

        except(ValueError):
            print('\nError, integers only\n')
        
if __name__ == "__main__":
    main()