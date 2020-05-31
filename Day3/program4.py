l = input('Enter elements in list seperated by space').split()
index = 0

for i in range(len(l)):
    for j in range(0, i+1):
        if (l[i] == l[j]):
            x = j
            break

    if (x == i):
        l[index] = l[i]
        index += 1
print("List after removing duplicate element is :",l[:index])
