[?1049h[?1h=[1;41r[?12;25h[?12l[?25h[27m[m[H[2J[?25l[41;1H"scrap_4i.py" 27L, 656C[1;1H[34m#!/usr/bin/python[m

[35mfrom[m lxml [35mimport[m html
[35mimport[m requests

[34m#https://en.wikipedia.org/wiki/List_of_universities_in_India
#page = requests.get('https://en.wikipedia.org/wiki/List_of_universities_in_India')[m

page = requests.get([31m'http://www.4icu.org/in/indian-universities.htm'[m)
tree = html.fromstring(page.content)

[34m#listOfUni = tree.xpath('//div[@class="col"]/table/tbody/tr/td/a/text()')

#listOfUni = tree.xpath('//table//tr/td/a/text()')[m

listOfUni = tree.xpath([31m'//td[@class="i"]/a/text()'[m)
[34m#print( listOfUni )[m

[36mprint[m [36mlen[m(listOfUni)

[34m#for uni in listOfUni:
#       print "Name: ", uni


#listOfNames = tree.xpath('//table//tr/td/h5/text()')
#print(listOfNames)[m

[1m[34m~                                                                                                                                                 [29;1H~                                                                                                                                                 [30;1H~                                                                                                                                                 [31;1H~                                                                                                                                                 [32;1H~                                                                                                                                                 [33;1H~                                                                                                                                                 [34;1H~                                                                                                                                                 [35;1H~                                                                                                                                                 [36;1H~                                                                                                                                                 [37;1H~                                                                                                                                                 [38;1H~                                                                                                                                                 [39;1H~                                                                                                                                                 [40;1H~                                                                                                                                                 [m[41;129H1,1[11CAll[1;1H[?12l[?25h[?25l[41;1HType  :quit<Enter>  to exit Vim[41;129H[K[41;129H1,1[11CAll[1;1H[?12l[?25h[?25l[41;129H[K[41;129H1,1[11CAll[1;1H[?12l[?25h[41;1H[?1l>[?1049lVim: Error reading input, exiting...
Vim: Finished.
[41;1H[J3 files to edit
# python_examples
