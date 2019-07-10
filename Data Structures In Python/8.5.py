fname = input("Enter file name: ")

#comment the line below
fname = "mbox-short.txt"

if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From") and line.startswith("From:") is False:
        count += 1
        words = line.split()

        #guardain, even if starts with From, it may have no other word
        if len(words) < 2:
            continue

        print(words[1])

print("There were", count, "lines in the file with From as the first word")
