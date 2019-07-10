fname = input("Enter file name: ")
#for a little convinince, comment it
fname = "romeo.txt"
fh = open(fname)

lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
