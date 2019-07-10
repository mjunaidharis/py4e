from bs4 import BeautifulSoup
import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

#url = input('Enter - ')
#url = "https://docs.python.org"
url = "http://py4e-data.dr-chuck.net/known_by_Travis.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)

for i in range(6):
    print( list(tags[17].attrs.values())[0] )
    url = list(tags[17].attrs.values())[0]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
print (tags[17].contents[0])
