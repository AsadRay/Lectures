#the time.time() function
#----> returns the number of seconds since that moment as a float value. 
import time
import datetime
'''If you call time.time() at the beginning of the code block you want to measure and again at the end,
 you can subtract the first timestamp from the second to find the elapsed time between those two calls.'''

print(time.time())
def calcProd():
    product = 1  
    for i in range(1, 100000):  
        product = product * i  
    return product  

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))   

print(time.ctime())#--->time.time()is not human readable so time.ctime() better to use to see the current time

#The time.sleep() Function
for i in range(3):
    print('Tick')
    time.sleep(2)
    print('Tock')
    time.sleep(2)
    print('GAME OVER!!')

time.sleep(5)

#Rounding Numbers
#we use it to helps shorten float values to make them easier to read and use. by round(number, digits)
now = time.time()
print(now)
print(round(now,2))
print(round(now))

#PROJECT SUPER STOPWATCH
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # Wait for user to start
print('Started.')

startTime = time.time()  # Start the stopwatch
lastTime = startTime
lapNum = 1  # Lap counter

try:
    while True:
        input()  # Wait for user input to mark a lap
        lapTime = round(time.time() - lastTime, 2)  # Time since last lap
        totalTime = round(time.time() - startTime, 2)  # Total time since start

        print(f'Lap #{lapNum}: {lapTime} seconds (Total: {totalTime} seconds)')  # Display lap details
        
        lastTime = time.time()  # Reset last lap time
        lapNum += 1  # Increase lap number

except KeyboardInterrupt:
    print('\nDone.')  # Gracefully exit when Ctrl-C is pressed

#The DateTime Module

import datetime
print(datetime.datetime.now()) 
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print('Year:' + str(dt.year) + '\n',
      'month:' + str(dt.month)+ '\n',
      'day:' + str(dt.day)+ '\n',
      'hour:' + str(dt.hour)+ '\n',
      'minute:' + str(dt.minute)
      )
      
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019> newyears2020)
print(newyears2020>halloween2019)
print(newyears2020 != oct31_2019)

#The timedelta Data Type --->A timedelta object represents a duration, i.e., the difference between two dates or times. It is part of the datetime
delta = datetime.timedelta(days=11, hours=24, minutes=9, seconds=8)
print(delta.days , delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))
dt = datetime.datetime.now()
thousand = datetime.timedelta(days=1000)
print(dt + thousand)

#pausing until a specific date
halloween2016 = datetime.datetime(2016, 10 ,31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)  # Wait 1 second before checking again


#Converting datetime Objects into Strings
# %Y  - Year with century, as in '2014'
# %y  - Year without century, '00' to '99' (1970 to 2069)
# %m  - Month as a decimal number, '01' to '12'
# %B  - Full month name, as in 'November'
# %b  - Abbreviated month name, as in 'Nov'
# %d  - Day of the month, '01' to '31'
# %j  - Day of the year, '001' to '366'
# %w  - Day of the week, '0' (Sunday) to '6' (Saturday)
# %A  - Full weekday name, as in 'Monday'
# %a  - Abbreviated weekday name, as in 'Mon'
# %H  - Hour (24-hour clock), '00' to '23'
# %I  - Hour (12-hour clock), '01' to '12'
# %M  - Minute, '00' to '59'
# %S  - Second, '00' to '59'
# %p  - 'AM' or 'PM'
# %%  - Literal '%' character

#Multithreading
startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
# Keep checking if the current time is before the startTime
while datetime.datetime.now() < startTime:
    time.sleep(1)  # Wait 1 second before checking again
# Once the current time is equal to or after startTime, it will print
print('Program now starting on Halloween 2029')

import threading, time
print('Start of Program.')
def takeANap():
    time.sleep(5)
    print('Wake up!!')
threadObj = threading.Thread(target=takeANap) 
threadObj.start() #--->This starts the thread. When you call start(), Python runs the takeANap function in a separate thread concurrently with the main program. 
#This means the program doesn't need to wait for the takeANap function to finish (i.e., the 5-second nap) before it moves on to the next line of code.
print('End of program.')   
