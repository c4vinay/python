#program to read a string and return second word in upper
str="Virat vinay "
str1=str.split()
if len(str1)>=2:
    print(str1[1].upper())
else:
    print(str1)
