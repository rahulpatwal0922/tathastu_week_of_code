from itertools import permutations
string = input("enter a string")
print('All permutations of string are :')
for p in permutations(string):
    print(''.join(p))
