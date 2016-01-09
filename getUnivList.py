#!/usr/bin/python

from lxml import html
import requests
import csv

print ('Connecting to server...')

#get the page content
page = requests.get('http://www.4icu.org/in/indian-universities.htm')
tree = html.fromstring(page.content)


#get the universties name and Address from tress
uNames 	 = tree.xpath('//td[@class="i"]/a/text()')
uAddress = tree.xpath('//td[@class="i"]/h5/text()')


print ('processing data...')


#create a file handler
c = csv.writer(open("listOfUniversites.csv", "wb"))
c.writerow(["Name","Address"])

#Loop through all the content.
for index in range(len(uNames)):
	#print 'University Name: ', uNames[index], ' == Address: ',uAddress[index] 
	c.writerow([uNames[index],uAddress[index]])


print ('List Created Successfully!')
