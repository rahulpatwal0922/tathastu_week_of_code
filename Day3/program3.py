str= list(input("Enter a string"))
n = len(str)
index = 0
x=0
for i in range (n):
    for j in range(0,i+1):
        if(str[i] == str[j]):
            x=j
            break

    if(x == i):
        str[index]=str[i]
        index +=1
print("String after removing duplicate character is : ","".join(str[:index]))
