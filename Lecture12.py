'''
webbrowser Comes with Python and opens a browser to a specific page.

requests Downloads files and web pages from the internet.

bs4 Parses HTML, the format that web pages are written in.

selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.'''

import webbrowser
import requests
import bs4
webbrowser.open('https://www.github.com\AsadRay')

res = requests.get('https://raw.githubusercontent.com/AsadRay/Lectures/main/Lecture1.py')
print(type(res))
print(res)
print(res.text)
password = '12345'
username = 'AsadRay'
a1 = input('Enter your name: ')
a2 = input('Enter your password: ')
try:
    
    if a1 == username and a2 == password:
        webbrowser.open('https://www.github.com/AsadRay')
    else:
        print('Invalid Username or Password. Try again.')
        a1 = input('Enter your name (1st attempt): ')
        a2 = input('Enter your password (1st attempt): ')
        

    if a2 == password and a1 == username:

        webbrowser.open('https://www.github.com/AsadRay')
    else:
        print('Invalid Password and Username. Try again.')
        a4 = input('Enter your name (2nd attempt) : ')
        a3 = input('Enter your password (2nd attempt): ')
        
     
        if a3 == password and a4 == username:
            webbrowser.open('https://www.github.com/AsadRay')
        else:
            # Raise exception if both attempts are wrong
            raise ValueError("YOU ARE NOT THE REAL USER. GET LOST!!!")

# Exception block to handle the raised error
except ValueError as e:
    print(e)
#checking for Errors
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()


url = "https://example.com/somefile"

try:
    # Try to download the file
    response = requests.get(url)
    response.raise_for_status()  # This checks for errors

    # If no error, process the content
    print("Download successful!")
    
except requests.exceptions.HTTPError as err:
    # If there is an error (like 404 or 500), handle it here
    print(f"Error occurred: {err}")
    print("Failed to download the file.")

#saving downloaded files to the hard drive

res = requests.get('https://www.github.com/AsadRay')
res.raise_for_status()
playFile = open('AsadRay.html', 'wb')
for chunk in res.iter_content(100000):  #---> here iter_content() method that reads the content of the response in chunks(Piceces of data)
    playFile.write(chunk)
playFile.close()

#parsing html with the bs4 module
#Creating a BeautifulSoup Object from HTML
res = requests.get('https://www.github.com/AsadRay')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))
print(noStarchSoup.title.text)  # Prints the title of the page
print(noStarchSoup.find('a')) # Prints the first <a> tag

#finding an element with the select() method
'''
soup.select('div') --->All elements named <div>

soup.select('#author')---->The element with an id attribute of author

soup.select('.notice')--?All elements that use a CSS class attribute named notice

soup.select('div span')--->All elements named <span> that are within an element named <div>

soup.select('div > span')-->All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')--->All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')--->All elements named <input> that have an attribute named type with value button

✅ select('tag') → Find all elements with that tag (returns a list).
✅ str(element) → See the element as an HTML string.
✅ element.getText() → Extract just the text inside (removes HTML tags).
✅ element.get('attr') → Get an attribute value (e.g., id).
✅ element.attrs → See all attributes as a dictionary.'''

exampleFile = open('AsadRay.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
elems = exampleSoup.select('#author')
print(elems)
print(type(elems))
print(len(elems))
print(elems[0].getText())
print(elems[0].attrs)
#getting Data from an Element's Attributes
soup = bs4.BeautifulSoup(open('AsadRay.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)

from bs4 import BeautifulSoup

html = '<html><body><span id="author">Asad Ray</span></body></html>'
soup = BeautifulSoup(html, 'html.parser')

author = soup.find('span', id='author').text
print(author)  # Output: Asad Ray

#Project: Opening All Search Results
#Step 1: Get the Command Line Arguments and Request the Search Page
#! python3
# searchpypi.py  - Opens several search results.


print('Searching...')    # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.

#Step 2: Find All the Results
#! python3
# searchpypi.py - Opens several google results.
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

#Step 3: Open Web Browsers for Each Result
#! python3
# searchpypi.py - Opens several search results.
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)