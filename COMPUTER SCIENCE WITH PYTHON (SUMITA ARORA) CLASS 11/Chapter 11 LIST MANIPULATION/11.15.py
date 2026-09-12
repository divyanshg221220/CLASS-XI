#11.15
l1=eval(input("Enter first list:"))
l2=eval(input("Enter second list:"))
index=0
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        index=i
        break
print(index)