def Ks(W, weight, value, n):
    if n == 0 or W == 0:
        return 0
    if (weight[n - 1] > W):
        return Ks(W, weight, value, n - 1)
    else:
        return max(value[n - 1] + Ks(
                W - weight[n - 1], weight, value, n - 1),
            Ks(W, weight, value, n - 1))

n = int(input('enter number of items'))
value = []
weight = []
for i in range(n):
    value.append(int(input("enter value for item"+str(i+1)+" : ")))
    weight.append(int(input("enter weight for item" + str(i + 1) + " : ")))
W = int(input('enter total capacity of sack'))
print("maximum total value in knapsack is", Ks(W, weight, value, n))
