n= int(input('enter a number'))
for i in range(n):
    print( (str(n-i) + "*") * (n-i-1) + str(n-i))
for i in range(2,n+1):
    print( (str(i) + '*') * (i-1) + str(i))
