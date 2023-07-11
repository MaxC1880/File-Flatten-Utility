# File Directory Utility
This Python program acts as a file directory utility, providing functionality to flatten an entire system of files into a single directory or unflatten a single directory into a system of files. It utilizes a dictionary to store file paths for the operations.

## Installation
To use this program, follow the steps below:

1. Clone the repository or download the Python file to your local machine.
2. Ensure you have Python installed (version 3 or above).
3. Install the required dependencies by running the following command:

   pip install shutil tkinter


## Usage
1. Run the program by executing the Python script: "python file_directory_utility.py"

2. You will be presented with a menu of options:
  "Please select an option:
  0: Exit program
  1: Collapse directory to flat files
  2: Uncollapse flat files to directory"
  
3. Select the desired option by entering the corresponding number.


## Collapsing Directory to Flat Files
If you choose option 1, the program will prompt you to select the root directory and output directory using a file dialog. The root directory is the directory you want to flatten. The output directory is where the flattened files will be stored.

The program will generate a dictionary to store the original paths of the files. It will then flatten the entire directory structure into a single directory, using a naming convention based on the dictionary entries.

You will be asked whether you want to delete the original files after they are copied to the output directory. Enter 1 for "Yes" or 2 for "No."


## Uncollapsing Flat Files to Directory
If you choose option 2, the program will prompt you to select the root directory and destination directory using a file dialog. The root directory is the directory containing the flattened files, along with the DICTIONARY.txt file generated from the collapsing operation. The destination directory is where the uncollapsed directory structure will be created.

The program will read the DICTIONARY.txt file to obtain the original paths of the files. It will then recreate the directory structure and copy the files to their respective directories.

Similarly, you will be asked whether you want to delete the original files after they are copied to the destination directory. Enter 1 for "Yes" or 2 for "No."


## Extras
The other program atteched is a simple script that allows a user to gather every file in a system of directories that ends with a certain extension like '.html' or '.py'.
