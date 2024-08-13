str=input("Enter a string:")
str1=""
for i in str:
    if i.isupper():
        str1=str1+i.lower()
    elif i.islower():
        str1=str1+i.upper()
    else:
        str1=str1+i
print(str1)
