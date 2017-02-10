import urllib2
import re
from bs4 import BeautifulSoup

## Poem Scraper

response = urllib2.urlopen('https://www.poemhunter.com/william-blake/poems/')

# print(response)
soup = BeautifulSoup(response, 'html.parser')

# print(soup.prettify())
links = soup.select(".poems a[href]")

print links

for number in range(2, 5):
  res = urllib2.urlopen('https://www.poemhunter.com/william-blake/poems/page-{number}/')
  nextSoup = BeautifulSoup(res, 'html.parser')

  for poem in nextSoup:
    links.append(poem)





print  '-------------------------------------------------------------'
print links
print links.length
# print nextSoup
# print soup.find(text=re.compile('Worldwide'))
# print soup.find_all('td')

# print jim.text


# print pattern
# m = re.search(pattern, jim.text)
# print m.group(0) == '$'



# for i in jim:
#   m = re.search(pattern, i.text)
#   print m
  # if i.text == m:
  #   print True
  # else:
  #   print False

# table = soup.table.tr

# # print table.find_next('td').a['href']

# table_array = table.find_all_next('td')

# link_array = []


# for link in table_array:
#   # link_array.append(link.a.get('href'))
#   link_array.append(link.a)


# for link in link_array:
#   if link != None:
#     print link['href']
    # print link['href']


# print link_array

# for link in soup.find_all('tbody'):
#   print(link)



# class Scraper:

#   def __init__(self, url):
#     self.url     = url
#     self.data    = None
#     self.element = None

#   def getData(self):
#     response = urllib2.urlopen(self.url)
#     self.data = BeautifulSoup(response, 'html.parser')
#     return self.data

#   def findElement(self, element):
#     if(self.data):
#       foundElement = self.data.find_all(self.element)
#       return foundElement
#     else:
#       foundElement =  self.getData().find_all(element)



# carbon = Scraper('https://en.wikipedia.org/wiki/Carbon')

# print carbon.findElement('td')



