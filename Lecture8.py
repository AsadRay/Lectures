#The PyInputPlus Module
import pyinputplus as pyip
import re
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')
#The PyInputPlus Module
import pyinputplus as pyip
response = pyip.inputNum()
print(response)

response = pyip.inputInt('Ener Num: ', min=4, lessThan=6)
print(response)

def inputEmail():
    emailRegex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    while True:
        email = input('Enter your email: ')
        if emailRegex.search(email):
            return email
        print('Invalid email address.')
email = inputEmail()
print(f"Your email: {email}")


import pyinputplus as pyip

try:
    response = pyip.inputNum('Enter num: ', timeout=5)
    print('Your Number:', response)  # This runs only if input is given in time
except pyip.TimeoutException:
    print('Account Locked.')  # Handles timeout error   

response = pyip.inputNum(limit=2, default='N/A')
print(response)

response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)
response = pyip.inputNum(blockRegexes=[r'[02485]$'])
print(response)
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)


response = pyip.inputStr(allowRegexes=[r'cat mama' ,'dog mama'], blockRegexes=[r'cat'])
print(response)

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)
response = pyip.inputCustom(addsUpToTen) 
print(response)

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day.')