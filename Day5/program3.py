n = int(input('Enter number of houses'))
house =[0]
for i in range(n):
    house.append(int(input('Enter money in house number'+str(i+1))))

maximum = max(house)
money = 0
for i in range(n//2):
    for j in range(n+1):
        if(house[j] == maximum):
            money += maximum
            if(maximum == house[-1]):
                house[-2] = 0
                house[-1] = 0
            else:
                house[j-1] = 0
                house[j] = 0
                house[j+1] = 0
        else:
            pass
    maximum = max(house)
print(' Maximum amount of money stolen by the theif is',money)
