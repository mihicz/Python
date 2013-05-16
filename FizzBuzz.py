#!/usr/bin/env python3
for n in range(1, 101):
  x = [n,'Fizz','Buzz','FizzBuzz']
  print(x[int('{:d}{:d}'.format(n%5==0,n%3==0),2)])
