def Small(arr, n):
    result = 1

    for i in range(0, n):
        if arr[i] <= result:
            result = result + arr[i]
        else:
            break
    return result
arr1 = [1, 2,5, 7]
n1 = len(arr1)
print(Small(arr1, n1))
