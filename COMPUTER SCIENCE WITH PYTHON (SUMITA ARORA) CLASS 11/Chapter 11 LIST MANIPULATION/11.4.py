#11.4
l=eval(input("Enter a list (1-12):"))
for i in range(len(l)):
    if l[i]>10:
        l[i]=10
print(l)