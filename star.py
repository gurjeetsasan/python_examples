#!/usr/bin/python

level = 10

for i in range(0, level):
	star = '';
	for j in range( i, 0, -1):
		star = star+'*' 		
	print star;
