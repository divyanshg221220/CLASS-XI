#11.5
l1=eval(input("Enter a list of strings:"))
l2=[]
for i in l1:
    l2.append(i[1:])
print(l2)