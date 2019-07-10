import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Access Service API
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
# Loop
while True:
   # address = input('Enter location: ')
    #address = "South Federal University"
    address = "Politehnica University Bucharest"

    # If input = 0, end loop
    if len(address) < 1:
        break

    # Encodes using urlencode using a dictionary
    url = serviceurl + urllib.parse.urlencode({'key': 42, 'address': address})

    # Print URL
    print('Retrieving', url)

    # Open and read URL
    data = urllib.request.urlopen(url).read()

    print('Retrieved', data, 'characters')

    # Try and except for bad data handling
    # json.loads loads data
    try:
        js = json.loads(data)
    except:
        print("Exception agae")
        js = None

    # Using json library, dump string using .dumps
    # Parse dictionary js
    # indent = 4: print it out nicely with indent of 4
    #print(json.dumps(js, indent=4))

    location = js['results'][0]['place_id']
    print(location)

    break