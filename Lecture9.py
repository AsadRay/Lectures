from pathlib import Path
p=Path('sapm', 'bacon', 'eggs') 
print(p)
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
#using the / operator to join paths
path = Path('spam') / 'bacon' / 'eggs'  
path = Path('spam') / Path('bacon/eggs')
print(path)
homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))
#The Current Working Directory
import os
ppp=Path.cwd()
print(ppp)
ppp=Path.home()
print(ppp)
#Creating New Folders Using the os.makedirs() Function
#p=Path(r'C:\Users|AI\spam').mkdir()
#print(p)
#Handling Absolute and Relative Paths
p=Path.cwd().is_absolute()
print(p)
p=Path.cwd() / Path('my/relative/path')
print(p)

# Relative path
relative_path = "docs/filename.txt"
# Convert to absolute path
absolute_path = os.path.abspath(relative_path)
print(absolute_path)
path1 = "/home/user/project"
path2 = "docs/filename.txt"
print(os.path.isabs(path1))
print(os.path.isabs(path2))
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
#Finding File Sizes and Folder Contents
#---->Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
#---->Calling os.listdir(path) will return a list of filename strings for each file in the path argument.

print(os.path.getsize(r'/home/asaduzzaman-rayhan/Lectures/Lecture9.py'))

#Opening Files with the open() Function
helloFile = open('/home/asaduzzaman-rayhan/Lectures/Lecture9.py')
print(helloFile)
#Reading the Contents of Files
helloContent = helloFile.read()
print(helloContent)
helloFile.close()
#Writing to Files
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
print(baconFile)
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
mydat = open('Rayhan.txt', 'w')
mydat.write('Hey guys this is Rayhan')
mydat.close()
mydat = open('Rayhan.txt')
content = mydat.read()
mydat.close()
print(content)
#Saving Variables with the shelve Module
import shelve  
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
#Saving variables with the pprint.pformat() function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()