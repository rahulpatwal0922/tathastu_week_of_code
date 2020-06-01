from collections import Counter
n = int(input('Enter the total number of votes'))
votes = []
l =[]
for i in range(n):
    votes.append(input("enter name of candidate that vote "))
count = dict(Counter(votes))
for key , value in count.items():
    x = max(count.values())
    if(count[key] == x):
        l.append(key)
min = l[0]
for i in range(len(l)-1):
    if(l[i+1]<min):
        l[i+1],min = min,l[i+1]
    else:
        continue
print("Candidate who received max number of votes is: ",min)
