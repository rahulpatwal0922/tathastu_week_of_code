l , m  = [],[]
n = int(input('enter size'))
arr =list(map(int,input("enter element seperated by space").split()))
for x in arr:
    if(x%2 == 0):
        l.append(x)
    else:
        m.append(x)
m.sort(reverse=True)
l.sort()
for x in l:
    m.append(x)
print("array after sort odd numbers in desending order and even numbers in assending order is ",m)
