Dict = []
size = int(input("enter size of dictionary"))
print('Enter words in dictionary one by one')
for i in range(size):
    Dict.append(input("word"+str(i+1)+" :"))
n = int(input('enter size of array'))
arr = []
print('enter character in array one by one')
for i in range(n):
    arr.append(input("enter character"+ str(i+1) +": "))
for word in Dict:
    if(set(word).issubset(set(arr))):
        print(word,end=" ")
