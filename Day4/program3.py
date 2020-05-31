n = int(input("Enter number of elements you want in dictionary"))
dictionary={}
for i in range(n):
    x = input("enter key")
    y = input('enter value')
    dictionary[x]=y

print("Second largest value in dictionary is :",list(sorted(dictionary.values()))[-2])
