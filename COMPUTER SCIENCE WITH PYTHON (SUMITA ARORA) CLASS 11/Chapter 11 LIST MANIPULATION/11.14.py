#11.14
l=eval(input("Enter a list:"))
unique=[]
duplicate=[]
for i in l:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
l=unique+duplicate
print(l)