'''def hello():
    print("Hell o, world!")
    print("howdy")
    print("hello there")
hello()'''
'''
def hello(name):
    print("Hello, " + name + "!")
hello('Alice')
hello('Bob')       

def sayHello(name):
    print("Hello, " + name + "!")
sayHello('Alice')    

def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(5, 3)
print("The sum is:", result)

def a(name):
    print(len('Rayhan'))
a('example')
######Return Values and return Statements######
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune) 
print(getAnswer(random.randint(1,9)))

spam = print('Hello!')
print(None == spam)
print('Hello', end='')
print('World')
print('cats', 'dogs', 'mice', sep=',')
##########The Call Stack##########
def a():
    print('a()starts')
    b()
    d()
    print('a()returns')
def b():
    print('b()starts')
    print('b()returns')
    c()
def c():
    print('c()starts')
    print('c()returns')
def d():
    print('d()starts')
    print('d()returns')
a()

########global statement########
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

def spam():
    global eggs
    eggs = 'bacon' #this is the global
def bacon():
    eggs ='spam' #this is a local
def ham():
    print(eggs) #this is the global
eggs = 42 #this is the global
spam()
print(eggs)    '''
#########Exception Handling########
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(-1))   