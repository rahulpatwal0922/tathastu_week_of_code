Tuples = int(input('Enter number of tuples '))
n = int(input('Enter size of each tuple '))
List = []
for i in range(Tuples):
    L = []
    print("Tuple "+str(i+1)+":")
    for j in range(n):
        L.append(int(input('Enter element '+str(j+1)+": " )))
    List.append(tuple(L))

index = int(input('Enter index of nth element of tuple about which you want to sort'))
List.sort( key = lambda x: x[index])
print("after sorting tuples list by nth index : ", List)
