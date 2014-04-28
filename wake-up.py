#! /usr/bin/env python
# simple script for alarm clock
# arguments:
#   "Tea is done" - some text
#   5m  - delay time

#TODO:
# - end time input option as absolute time (obviously greater than current time), e.g. 18:30
# - counting time?
# - after alarm done, ring until someone hit computer with hammer?
# - alarm with some mp3 file?

import sys
import re
import time

# --- Definitions ---

def getMessage(text):
    if not isinstance(text,str):
        sys.exit('Error: not a string!')
    return text

def getTime(string):
# check time string format with regular expresions
# float number and one of chars {s,m,h}

    getMessage(string)

    pattern = re.compile('^[0-9]+\.?[0-9]*(s|m|h)$')
    if not pattern.match(string):
        sys.exit('Error: bad time format!')

    power = {'s' : 1, 'm' : 60, 'h' : 60*60}
    delay = float(string[:-1]) * power[string[-1]]
    # NOTE: strange, input string "0.0001h" will get value delay 0.36000000000000004, precision?

    return delay

# --- check input arguments --- 

#print('Input arguments:')
#for i in sys.argv:
    #print (i)

l =  len(sys.argv)-1
if l == 0:
    message = getMessage(input('Enter a message: '))
    delay = getTime(input('Enter a time delay: '))
elif l == 1:
    delay = getTime(sys.argv[1])
    message = "Alarm! Wake-up!"
elif l == 2:
    delay = getTime(sys.argv[2])
    message = getMessage(sys.argv[1])
else:
    sys.exit('Usage: %s "Some text" 5m' % sys.argv[0])


#print(message)
#print(delay)

time.sleep(delay)
print(message,'\a')






