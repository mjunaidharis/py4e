import lxml.etree as ET
import urllib.request
from bs4 import BeautifulSoup

#Hit request
url = "http://py4e-data.dr-chuck.net/comments_261479.xml"
print ('Retrieving', url)
html = urllib.request.urlopen(url).read()

#Count length of data
print ('Retrieving %d characters' % (len(html)))

stuff = ET.fromstring(html)

lst = stuff.findall('.//comment')
print('User count:', len(lst))          

total = 0

for item in lst:
    count = item.find('count').text
    count = int(count)
    total += count

print (total)
