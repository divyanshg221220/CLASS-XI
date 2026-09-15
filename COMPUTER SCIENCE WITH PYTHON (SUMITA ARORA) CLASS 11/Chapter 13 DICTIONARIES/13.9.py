#13.9
D1=eval(input("Enter first dictionary:"))
D2=eval(input("Enter second dictionary:"))
l=[]
for i in D1:
    if i in D2:
        l.append(i)
print(l)