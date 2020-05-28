n= int(input("enter an even number"))
for i in range(n):
    for j in range(n):
        if(i == j):
            print("*",end="")
        elif(i == n-1-j):
            print("*", end="")
        else:
            print(" ",end="")
    print()
