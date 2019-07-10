import json
import urllib.request

#url = input('Enter location: ')
url = "http://py4e-data.dr-chuck.net/comments_261480.json"
print ('Retrieving', url)

#Reading data
data = urllib.request.urlopen(url).read()
print ('Retrieved', data)

#parsing
jsp = json.loads(data)

#we have a dictionary where value of each key is a list
#list of dictionary

l = list()
#iterate throught the (value)list of key 'comments'
for u in jsp['comments']:
    #a list of dictionary
    num = int(u['count'])
    l.append(num)

print ('Count:', len(l))
print ('Sum:', sum(l))
