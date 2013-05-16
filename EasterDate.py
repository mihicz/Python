#!/usr/bin/env python
#import sys
#import string
from datetime import date

#----------------------------------------
def getEasterDate(year):
	# get catolic Easter date

	a = year%19; b = year%4; c = year%7;
	m = 24; n = 5;
	d = (19*a + m)%30
	e = (n + 2*b + 4*c +6*d)%7

	day = d + e - 9
	if day==25 and d==28 and e==6 and a>10 :
		day = 18
		month = 4
	elif day>=1 and day<=25 :
		month = 4
	elif day>25 :
		day = day-7
		month = 4
	else:
		day = 22 + d + e
		month = 3

	return date(year,month,day);
#----------------------------------------
# main
#def main():
#if __name__ == "__main__":

today = date.today()
year = input("Zadej rok: ")
if	not(str.isdigit(year)):
	print ("Chyba: rok musi byt zadan jako cele cislo!")
	exit()

Easter = getEasterDate(int(year))

if Easter == today: 
	print("Dnes jsou Velikonoce.")
elif Easter < today:
	print("V roce {} byli Velikonoce {}.{}.".format(Easter.year,Easter.day,Easter.month))
else:
	print("V roce {} budou Velikonoce {}.{}.".format(Easter.year,Easter.day,Easter.month))

