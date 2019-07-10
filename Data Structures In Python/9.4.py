def f2(d1):
    return [(v,k) for k,v in d1.items() if v == max(d1.values())][0]


name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"

fh = open(name)
dic = dict()

for lines in fh:
    if lines.startswith("From") and lines.startswith("From:") is False:
        words = lines.split()

        if len(words) < 2:
            continue

        # if the person appeared for the first time, add him to dictionary with count 1
        if dic.get(words[1], 0) == 0:
            dic[words[1]] = 1
        # increment the count
        else:
            dic[words[1]] = dic.get(words[1]) + 1
max_word = f2(dic)
stringg = str(max_word[1]) + ' ' + str(max_word[0])
print(stringg)