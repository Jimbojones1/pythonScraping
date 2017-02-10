import urllib2
import re
from bs4 import BeautifulSoup

## Poem Scraper

response = urllib2.urlopen('https://www.poemhunter.com/william-blake/poems/')

# print(response)
soup = BeautifulSoup(response, 'html.parser')

# print(soup.prettify())
links = soup.select(".poems a[href]")

# stored poem links
poemLinks = []

# getting links for the first page since it doesn't have page number to lazy to concat
for poem in links:
  p = poem.get('href')
  poemLinks.append(p)


# getting links for pages 2, 5
for number in range(2, 5):
  res = urllib2.urlopen('https://www.poemhunter.com/william-blake/poems/page-{number}/')
  nextSoup = BeautifulSoup(res, 'html.parser')

  linkTitles = nextSoup.select('.poems a[href]')

  for poem in linkTitles:
    p = poem.get('href')
    poemLinks.append(p)




#getting all the poems

poemDic = {}

poemPage = urllib2.urlopen('https://www.poemhunter.com' + poemLinks[0] + '/')

poemSoup = BeautifulSoup(poemPage, 'html.parser')

# print poemSoup.prettify()

# this code extracts the poem as a string
container = poemSoup.select('.KonaBody')
f = container[0].p.__str__().strip()
fp = f.split('<p>\r\n')[1].strip()
finalPoemString = fp.split('\r\n')[0].strip()
poemDic['poem'] = finalPoemString



title    = poemSoup.select('#solSiirMetinDV h1')
strTitle = title[0].getText().__str__()
author = strTitle.split('-')[1].split('by')[1].strip()

# print strTitle.split('-')[0].strip()

poemDic['title']  = strTitle.split('-')[0].strip()
poemDic['author'] = author
 # author = myStr.split('-')[1].split('by')[1].strip()

print  '-------------------------------------------------------------'
print poemDic


concatString = 'https://www.poemhunter.com' + poemLinks[0]

# print concatString
# print poemLinks[0]
# somePract = urllib2.urlopen(concatString)

# s = BeautifulSoup(somePract, 'html.parser')

# print(s.prettify())















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



