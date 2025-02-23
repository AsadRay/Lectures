print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
print(r'That is Carol\'s cat.')#raw string


spam = 'Hello world!'
print(spam[:4])
print(spam[0:5])
print('Hello' in spam)
print('Hello' not in spam)
name = 'Al'
age = 3000
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
print('My name is %s. I am %s years old.' % (name, age))

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

print('Hello'.upper().lower().upper().lower())    
spam="HELLO"
print(spam.islower())
print(spam.isupper())
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is Not Title Case Either'.istitle())

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

print(' Name Is Roko'.startswith('My'))#--> startswith()
print(' Name Is Roko'.endswith('Roko'))#--> endswith()
sp=' '.join(['My', 'name', 'is', 'Simon'])#--> join()
print(sp)
sp='+'.join(['My', 'name', 'is', 'Simon'])#--> join()
print(sp)
print('Hello, world!'.partition('o'))
print('Hello, world!'.partition('e'))
print('hello'.center(10))
print('hello'.rjust(10))
print('hello'.ljust(10))
print('hello'.rjust(20, '*'))
print('hello'.ljust(20, '-'))
print('hello'.center(20, '='))
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
printPicnic(picnicItems, 10, 10)
printPicnic(picnicItems, 15, 5)
printPicnic(picnicItems, 20, 10)
#Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
spam = '      Hello, World!  '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())