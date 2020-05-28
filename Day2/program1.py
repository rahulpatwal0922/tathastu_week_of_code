n = int(input("enter a number"))
count ,sum,new =0,0,""
num ,pnum=n,n

for i in range (2,n//2):
    if(n%i == 0):
        count+=1
while (num != 0):
    r = num%10
    num = num//10
    sum += r**3

while (pnum!= 0):
    r = pnum%10
    pnum = pnum//10
    new+= str(r)

if(n%2 == 0):
    print("number is even")
else:
    print("number is odd")
if(count == 0):
    print("number is prime")
if(int(new) == n):
    print("number is palindrome")
if(int(sum) == n):
    print("number is armstrong number")
