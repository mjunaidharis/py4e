from bs4 import BeautifulSoup
import ssl
import urllib.request
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

#url = input('Enter - ')
#url = "https://docs.python.org"
url = "http://py4e-data.dr-chuck.net/comments_261477.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
#print(tags)

for tag in tags:
    #print("huii")
    #print(tag.get('href', None))
    number = tag.contents[0]
    number = int(number)
    total += number

print (total)
