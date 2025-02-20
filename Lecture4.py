
def spam(animal):
    animal[:] = ['cat', 'dog', 'fish', 'bird','dog']

# Define an empty list
animal = []

# Call the function with the global list
spam(animal)

# Print the first element of the list
print(animal[2]) #----> Indexing
print(animal[-3]) #----> Negative Indexing
print(animal[0:2]) #----> Slicing
print(animal[1:4:2]) #----> Slicing with step
print('this is my',animal[0],'Meet his friend kallu',animal[1]) #----> Concatenation
print(len(animal)) #----> Length of the list
print(animal.count('dog')) #----> Count of the element

animal[4]='Kiddo' #----> Updating the element
print(animal)

spam1=['cat', 'dog', 'fish', 'bird','dog']
spam2=['cat', 'dog', 'fish', 'bird','dog']
conc=spam1+spam2 #----> Concatenation
print(conc)
print(animal[4])
newlist= spam1+spam2+animal+['kiddo','middo','liddo'] 
print(newlist)
del spam1[1:3]
print(spam1)

# Asking for how many cats
print("Enter how many cats you have")
num_cats = int(input())  # Take the number of cats as input and convert it to an integer

# Create an empty list to store cat names
cats = []

# Loop to take input for each cat's name
print("What are their names?")
for i in range(num_cats):
    cat_name = input(f"Enter name of cat {i+1}: ")  # Prompt for each cat's name
    cats.append(cat_name)  # Append the name to the list

# Print the names of the cats
print("Here are the names of your cats:")
for name in cats:
    print(name)
    
print('ray'in ['hello','hi','howdy','hey'])

mypets=['cat','dog','fish','bird']
print('Enter a pet name')
name=input()
if name not in mypets:
    print('I do not have a pet named',name)
else:
    print('I have a pet named',name)

for i in range(1,6):
    print(i)
    if i==2:
        break
print('Done')
for i in range(1,6):
    if i==2:
        continue
    print(i)
print('Done')

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
for i in range(len(cats)):
    print('My cats ' + str(i) + ' they are ' + cats[i])

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))
spam.append('Rayhan')
print(spam)
spam.insert(1, 'Rayhan')
print(spam)
spam.remove('Rayhan')
print(spam)
spam.remove('Rayhan')
print(spam)

spam = [7,8,9,10,1,2,3,4,5,6]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
        
name = 'rayhan'
print(name[0:5:2])

# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.
    
name = list('Rayhan')
print(name)
name[1:3] = ['a', 'y']
print(name)
print(sorted(name, reverse=True))
print(name)
