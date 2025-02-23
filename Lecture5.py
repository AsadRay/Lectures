
mycat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(mycat['color'])#----->Dictorionary Datatype
print('My cat has a beautfiul color and that is ' + mycat['color'] + ' He is very ' + mycat['disposition'])
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
print(spam is bacon)
print(id(spam))
print(id(bacon))
print(id(spam) == id(bacon))
print(id(spam) != id(bacon))
spam = {'color': 'red', 'age': 42}
for v in spam.values():
     print(v)
spam = {'color': 'red', 'age': 42}
for v in spam.keys():
     print(v)


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0)
 count[character] = count[character] + 1

print(count)    

brithdays = {'Rayhan': 'Oct 13', 'Rayhum': 'Sep 08', 'Rana': 'Oct 15'}
while True:
     print('Enter a name to find their birthday: (blank to quit')
     name = input()
     if name == '':
          break
     if name in brithdays:
          print(brithdays[name] + ' your birthday is on ' + name)
     else:
          print('Sorry i cant find birhtday for' + name)
          print("But i can add to the list so that i can remember it")
          print('Enter your birthday')
          bday = input()
          brithdays[name] = bday
          print('Birthday database updated')
          print(brithdays)
          print('Thanks for the information')
          print('Now i can remember your birthday')

picnicItems = {'apples': 5, 'cups': 2}
print(' I am bringing ' + str(picnicItems.get( 'cups',0)) + ' cups ')
print(' I am bringing ' + str(picnicItems.get( 'apples',0)) + ' Apples ')
print(' I am bringing ' + str(picnicItems.get( 'eggs',0)) + ' Eggs ')
print(' I am bringing ' + str(picnicItems.get( 'milk',0)) + ' Milk ')

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('Color', 'Black')      
print(spam)
spam.setdefault('Color', 'White')
print(spam) 
 
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
     count.setdefault(character, 0)
     count[character] = count[character] + 1
pprint.pprint(count)

# tic-tac-toe game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
     print('-+-+-')
     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
     print('-+-+-')
     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
     printBoard(theBoard)
     print('Turn for ' + turn + '. Move on which space?')
     move = input()
     theBoard[move] = turn
     if turn == 'X':
          turn = 'O'
     else:
          turn = 'X'
printBoard(theBoard)
print('Game Over')
print('Thanks for playing')
print('Hope you enjoyed it')
print('See you again')
print('Goodbye')

allguests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
     numBrought = 0
     for k, v in guests.items():
          numBrought = numBrought + v.get(item, 0)          
     return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allguests, 'apples')))
print(' - Cups           ' + str(totalBrought(allguests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allguests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allguests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allguests, 'apple pies')))


   
