name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
    # if line starts with From only, then we will proceed
    if line.startswith("From") and line.startswith("From:") is False:
        words = line.split()

        # now guardain to protect us if line does not have time
        if len(words) < 6:
            continue

        # get the time
        word = words[5].split(":")

        # Add count to dictionary
        # If it already exists, add 1 to the count
        # Else creates new one, start with 0 and add 1
        dic[word[0]] = dic.get(word[0], 0) + 1

# Convert dictinoary to tuples,as assg is for tuples
counts = dic.items()

# sort the items, ascending order
counts = sorted(counts)

# print them
for k, v in counts:
    # simply to print k,v => have to do this because of python 2
    stringg = str(k) + ' ' + str(v)
    print(stringg)


