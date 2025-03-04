#reader Objects
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[6][1])

#Reading data from reader objects in a loop
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


#writer Objects 
outputFile = open('output.csv' , 'w' , newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam' , 'eggs' , 'bacon' , 'ham'])
outputWriter.writerow(['Hello , world!' , 'eggs' , 'bacon' , 'ham'])
outputWriter.writerow([1,2,3.141592,4])
outputFile.close()

output = csv.reader(outputFile)
outputRead = list(output)

#The delimiter and lineterminator Keyword Arguments
'''The delimiter and lineterminator keyword arguments in the csv.
writer function allow you to control how the data is written to the file, 
providing more flexibility than just using commas and newlines.'''
csvFile = open('example.tsv', 'w', newline='')  # Opens a new file for writing
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')  # Creates a CSV writer object
# Writing data to the file
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()  # Closes the file
#DictReader
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
# This loop prints each row's columns as values with their header names as keys
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
#---> the output will be like
'''4/5/2015 13:34 Apples 73
4/5/2015 3:41 Cherries 85
4/6/2015 12:46 Pears 14
4/8/2015 8:59 Oranges 52
4/10/2015 2:07 Apples 152
4/10/2015 18:10 Bananas 23
4/10/2015 2:40 Strawberries 98
'''

#DictWriter
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()  # Write the header row
# Write rows using dictionaries
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
outputFile.close()

#JSON and APIs
#Reading JSON with the loads() Function
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

#Writing JSON with the dumps() Function
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData