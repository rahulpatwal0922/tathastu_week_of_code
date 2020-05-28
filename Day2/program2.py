n = int(input("enter number upto you want to print fibonacci series"))
a = 0
b = 1
for i in range(n):
    c = int(a) + int(b)
    print(c,end=" ")
    a = b
    b = c
