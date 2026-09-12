#11.9
l=eval(input("Enter a list:"))
n=l[-1]
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=n
print(l)