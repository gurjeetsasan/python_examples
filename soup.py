from bs4 import BeautifulSoup
import urllib
#r = urllib.urlopen('http://yahoo.com/').read()

r = urllib.urlopen('https://en.wikipedia.org/wiki/Category:PHP_frameworks').read()
#https://en.wikipedia.org/wiki/Category:PHP_frameworks

soup = BeautifulSoup(r)
print type(soup)

letters = soup.find_all("ul")


#letters = soup.find_all("div", class_="Pos-a")
#letters = soup.find_all("div", id_="applet_p_32209491")

print type( letters )

#print letters 

for letter in letters:
	#print type(letter)
	#print letter.get_text()
	print letter.a.get_text()



#letters[0].a["href"]

#rint soup.prettify()

