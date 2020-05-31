L =input("enter elements of list 1 seperated by space").split()
M =input("enter elements of list 2 seperated by space").split()

L = set(L)
M = set(M)

intersection = L.intersection(M)
print("The intersection of lists is :",list(intersection))
