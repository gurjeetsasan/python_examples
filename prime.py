#!/usr/bin

# Code to check if number is Prime.

num_input = raw_input("Enter a number: ")

num 	= int(num_input)	 
flag 	= 'true' #true means not prime.

for i in range(2, num):
	if( num%i == 0):
		break;
	else:
		flag = 'false'


if( flag == 'true' ):
	print num,'is Not prime'
else:
	print num,'is prime'

 
print "Good Bye"
