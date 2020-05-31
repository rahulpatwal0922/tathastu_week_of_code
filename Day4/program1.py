from collections import Counter
n = int(input('enter number of elements in tuple'))
T = tuple(input('Enter elements seperated by space').split())

ele = input('enter element whose occurence you want to search')
O = Counter(T)
print(O[ele])
