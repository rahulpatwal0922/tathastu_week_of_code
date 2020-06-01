#remove duplicate values across dictionary values.
n = int(input("Enter number of elements you want in dictionary"))
base_dict={}
new_dict={}
for i in range(n):
    x = input("enter key for item "+str(i+1)+" :")
    y = input('enter value for item '+str(i+1)+" :")
    base_dict[x]=y

for key,value in base_dict.items():
    if (value not in new_dict.values()):
        new_dict[key] = value
print("Dictionary after removing duplicate values :",new_dict)
