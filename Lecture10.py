import shutil
import os
from pathlib import Path
# #Copying Files and Folders
import shutil
from pathlib import Path
import send2trash
import zipfile
'''
# Define the source path (the folder where 'spam.txt' is located)
p = Path('/home/asaduzzaman-rayhan/Lectures')

# Define the destination folder
destination_folder = p / '/home/asaduzzaman-rayhan/FILES'

# Make sure the destination folder exists
destination_folder.mkdir(parents=True, exist_ok=True)

# Copy the file 'Lecture9.py' from 'p' to 'FILES'
shutil.copy(p / 'Lecture9.py', destination_folder)
print(f"File 'Lecture9.py' copied to {destination_folder}")
rename = Path('/home/asaduzzaman-rayhan/FILES/Lecture9.py')

#Rename the file
# Define the source file
src = Path('/home/asaduzzaman-rayhan/Lectures/Lecture9.py')
# Define the destination folder and new name
dst_folder = Path('/home/asaduzzaman-rayhan/FILES')
new_name = 'NAMECHANGED.py'
# Make sure the destination folder exists
dst_folder.mkdir(parents=True, exist_ok=True)
# Define the full path for the new file in the destination folder
dst = dst_folder / new_name
# Copy the file to the new folder with a different name
shutil.copy(src, dst)
print(f"File moved and renamed to {dst.name} in {dst_folder}")

#permantly delete a file or folder
# Define the folder where you want to delete the contents
folder = Path('/home/asaduzzaman-rayhan/FILES')
# Iterate through the folder contents
for item in folder.iterdir():
    if item.is_file():
        item.unlink()  # Delete the file
    elif item.is_dir():
        shutil.rmtree(item)  # Recursively delete the folder and its contents
#----> this is the way to delete the folder but the folder should be empty
folder.rmdir()
print(f"All contents of the folder {folder} have been deleted.")

baconFile = open('bacon.txt', 'a')   # creates the file
baconFile.write('Bacon is not a vegetable.')
print(baconFile)
baconFile.close()
send2trash.send2trash('bacon.txt')   # deletes the file
#----> this is the way to delete the file by sending it to the trash

#Walking a Directory Tree
from pathlib import Path
# Define the directory you want to walk
directory = Path('/home/asaduzzaman-rayhan/Lectures')
# Use rglob() to recursively find all files and folders within the directory
for item in directory.rglob('*'):  # '*' means all files and directories
    print(item)  # Print each file or folder path

#creating and adding to zip files

# Define the folder and the file to zip
file_to_zip = Path('ada') / 'myCats.py'  # Path to your file
# Define the ZIP file path
zip_file = Path('myCats.zip')  # Name the zip file
# Create the ZIP file and add the file to it
with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Write the file to the zip, preserving its name
    zipf.write(file_to_zip, file_to_zip.name)
print(f"File '{file_to_zip.name}' has been zipped into {zip_file}")
'''
#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)                 # all text before the date
       ((0|1)?\d)-                                 # one or two digits for the month
       ((0|1|2|3)?\d)-                             # one or two digits for the day
       ((19|20)\d\d)                               # four digits for the year
       (.*?)$                                      # all text after the date
       """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    # Uncomment the following line to actually rename the files
    # shutil.move(amerFilename, euroFilename)
