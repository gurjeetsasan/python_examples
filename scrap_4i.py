#!/usr/bin/python

from lxml import html
import requests

#https://en.wikipedia.org/wiki/List_of_universities_in_India
#page = requests.get('https://en.wikipedia.org/wiki/List_of_universities_in_India')

page = requests.get('http://www.4icu.org/in/indian-universities.htm')
tree = html.fromstring(page.content)

#listOfUni = tree.xpath('//div[@class="col"]/table/tbody/tr/td/a/text()')

#listOfUni = tree.xpath('//table//tr/td/a/text()')

uNames 	 = tree.xpath('//td[@class="i"]/a/text()')
uAddress = tree.xpath('//td[@class="i"]/h5/text()')
#print( listOfUni )

#for uni in listOfUni:
#	print "Name: ", uni

for index in range(len(uNames)):
	print 'University Name: ', uNames[index], ' == Address: ',uAddress[index] 

#listOfNames = tree.xpath('//table//tr/td/h5/text()')
#print(listOfNames)

