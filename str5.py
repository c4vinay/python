#program to find the most repeated in a string
str=input("Enter a string:")
count={}
for i in str:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
rc=max(count,key=count.get)
freq=count[rc]
print("The most repeated character is {} which repeated {} times".format(rc,freq))
