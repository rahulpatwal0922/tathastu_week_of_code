def replace(num):
    return str(num).replace('0','5')

num = int(input('Enter an integer'))
print("Number after replacing 0 with 5 is",replace(num))
