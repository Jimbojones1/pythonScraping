import urllib2
from bs4 import BeautifulSoup


response = urllib2.urlopen('https://en.wikipedia.org/wiki/Carbon')

# print(response)
soup = BeautifulSoup(response, 'html.parser')

# print(soup.prettify())


print soup.table.find_all('tr')
