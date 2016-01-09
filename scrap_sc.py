#!/usr/bin/python

from lxml import html
import requests

#https://en.wikipedia.org/wiki/List_of_universities_in_India

#page = requests.get('http://www.4icu.org/in/indian-universities.htm')

page = requests.get('https://en.wikipedia.org/wiki/List_of_universities_in_India')
tree = html.fromstring(page.content)

#This will create a list of buyers:
schools = tree.xpath('//table[@class="wikitable"]')

#test = tree.xpath('/html/body/div[3]/div[3]/div[4]/table[1]/tbody/tr[1]/td[1]/a[1]/text()')
#titles = tree.xpath('//div[@title="buyer-name"]/text()')

titles = tree.xpath('//table[@class="wikitable"]/tbody/tr/td/text()') 


#print type(titles)

#print (titles)

firstHeading = tree.xpath('//h1[@class="firstHeading"]/text()')
#print (firstHeading)

#content = tree.xpath('//div[@id="mw-content-text"]/p/text()')
#print( content )

listOfUni = tree.xpath('//div[@id="mw-content-text"]/ul/li/b/a/text()')
print( listOfUni )

#schools = schools.xpath('//div[@class="maincontent"]')

#print schools



#print 'Buyers: ', buyers


#for b in buyers:
#	print b;




