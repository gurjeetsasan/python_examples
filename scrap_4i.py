#!/usr/bin/python

from lxml import html
import requests

#https://en.wikipedia.org/wiki/List_of_universities_in_India
#page = requests.get('https://en.wikipedia.org/wiki/List_of_universities_in_India')

page = requests.get('http://www.4icu.org/in/indian-universities.htm')
tree = html.fromstring(page.content)

#listOfUni = tree.xpath('//div[@class="col"]/table/tbody/tr/td/a/text()')

#listOfUni = tree.xpath('//table//tr/td/a/text()')

listOfUni = tree.xpath('//td[@class="i"]/a/text()')
#print( listOfUni )

print len(listOfUni)

#for uni in listOfUni:
#	print "Name: ", uni


#listOfNames = tree.xpath('//table//tr/td/h5/text()')
#print(listOfNames)

