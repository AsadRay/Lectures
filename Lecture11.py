import traceback
import logging

def user_input():
    try:
        a = input("Enter a two-digit number: ")
        if len(a) != 2 or not a.isdigit():
            raise Exception("No!!!! Enter a valid two-digit number")

        b = input("Enter another number: ")
        if b != a:
            raise Exception("No!!! Enter the same number that you entered before")

        c = input("Enter another number: ")
        if c != a:
            raise Exception("No!!! Enter the same number that you entered before for the first or second time")

        print("Oh my God! You've entered three valid numbers")
        print("The sum of the numbers is: ", int(a) + int(b) + int(c))

    except Exception as e:
        print("Invalid input Bruhhhh!! \n", e)

user_input()

#getting the traceback as a string
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')
spam()

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
    
#Assertions
#----> performed by assert statement
#----> if the condition is True, the program will continue to execute
#----> if the condition is False, the program will terminate
#----> assert statement is used to check the condition

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
ages.reverse()
assert ages[0] <= ages[-1]
print(ages)

def enter_club(age):
    assert age >= 18, "You must be at least 18 years old!"
    print("Welcome to the club!")

enter_club(20)  #  Works fine
enter_club(16)  #  Raises an AssertionError

#using an assertion in a traffic light simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'Yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)
switch_lights(market_2nd)
print('All good!!')

#---> if we use print() 
def switch_light(color):
    print(f"Changing light from {color}...")  # Debug message
    if color == "green":
        return "yellow"
    elif color == "yellow":
        return "red"
    elif color == "red":
        return "green"

light = "green"
light = switch_light(light)
print(f"Light is now: {light}")#--> for this program it will work fine but it will disspear after the program is done

#---> if we use logging
logging.basicConfig(level=logging.info)  # Set logging level

def switch_light(color):
    logging.info(f"Changing light from {color}...")  # Log message
    if color == "green":
        return "yellow"
    elif color == "yellow":
        return "red"
    elif color == "red":
        return "green"

light = "green"
light = switch_light(light)
logging.info(f"Light is now: {light}")  # Info message

#Using the logging Module
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

#logging levels
'''
DEBUG
logging.debug()
The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO
logging.info()
Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING
logging.warning()
Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR
logging.error()
Used to record an error that caused the program to fail to do something.

CRITICAL
logging.critical()
The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
'''