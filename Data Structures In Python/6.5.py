text = "X-DSPAM-Confidence:    0.8475";
num = 0.8475

#then find the starting of number, and pint till end
print(float(text[(text.find(str(num))):]))