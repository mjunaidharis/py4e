# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg, count = 0, 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    # print(line)

    # split the line on the basis of space
    words = line.split()

    # last word can be the float number we want
    try:
        no = float(words[-1])
        avg += no
        count += 1
    except:
        continue

if count != 0:
    avg /= count
print("Average spam confidence:", avg)
