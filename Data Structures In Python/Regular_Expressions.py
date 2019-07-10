import re

#First read the data form file
filename = "1.txt"
fh = open(filename)
sum = 0
for line in fh:

    #look for words having 0-9
    number = re.findall("[0-9]+",line)

    #Traverse through the list of numbers
    #and convert strings to Integer and keep accumulating
    for index in range(0,len(number)):
        sum += int(number[index])

print(sum)