#program to find the least repeated in a string
str=input("Enter a string:")
count={}
for i in str:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
rc=min(count,key=count.get)
freq=count[rc]
print("The least repeated character is {} which repeated {} times".format(rc,freq))
