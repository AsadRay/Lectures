#Finding Patterns of Text Without Regular Expressions
def isPhoneNumber(text):
    if len(text) != 14:  # Ensure the length is exactly 14
        return False
    if text[:4] != '+880':  # Ensure it starts with "+880"
        return False
    for i in range(4, 14):  # Ensure all characters after "+880" are digits
        if not text[i].isdecimal():
            return False
    return True 
print('+8801712345678 is a phone number:')
print(isPhoneNumber('+8801712345678'))
print('Hello is a phone number:')
print(isPhoneNumber('Hello'))

message = 'Call me at +8801712345678 tomorrow. +8801712349999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+14]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
#Matching Regex Objects
import re
phoneNumRegex = re.compile(r'\+880\d{10}')  
mo = phoneNumRegex.search('My number is +8801712659805.')
if mo:
    print('Phone number found:', mo.group()) 
else:
    print('No phone number found')
#Grouping with Parentheses
import re
phoneNumRegex = re.compile(r'(\+880)(\d{10})')  
mo = phoneNumRegex.search('My number is +8801712659805.')

if mo:
    print(mo.group(1))  
    print(mo.group(2))    
else:
    print('No phone number found')

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
#Matching Multiple Groups with the Pipe
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
#Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#Matching Zero or More with the Star
batRegex =re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
#Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
#Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
#Greedy and Nongreedy Matching  
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
#The findall() Method
phoneNumRegex = re.compile(r'\d{10}')
print(phoneNumRegex.findall('Cell: +8801712345678 Work: +8801712349999'))
#Character Classes
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#Negative Character Classes
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#The Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.') == None)
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)
#The Wildcard Character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
#Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
#Case-Insensitive Matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is parthuman.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
#Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
#Managing Complex Regexes
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)