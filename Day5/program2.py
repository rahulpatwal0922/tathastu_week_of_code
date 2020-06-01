arr = list(map(int,input("Enter element seperated by space").split()))
n = len(arr)
for i in range(n-1):
    great = max(arr[i+1:])
    arr[i]=great
print("Array after replacing each element with the greatest element on the right side",arr)
