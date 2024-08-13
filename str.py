#program to remove given word from string
str="VIRAT DHONI IS GREATEST OF ALL TIME"
word="DHONI"
str1=str.split()
result=[]
for i in str1:
    if i!=word:
        result.append(i)
print(*result)

        
