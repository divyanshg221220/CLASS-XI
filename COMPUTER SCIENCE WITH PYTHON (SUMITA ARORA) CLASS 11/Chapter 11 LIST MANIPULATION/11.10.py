#11.10
l=[0,1]
n=int(input("Enter the number:"))
if n<=20:
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    print(l[-1])
else:
    print("Upper limit of n to 20")