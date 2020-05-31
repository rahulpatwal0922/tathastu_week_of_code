s = input("enter a string")
s=s.split()
print("string after reversed in place is:",end=" ")
for i in range(len(s)):
    x = len(s[i])
    for j in range(-1,-x-1,-1):
        print(s[i][j],end="")
    print(" ",end="")
