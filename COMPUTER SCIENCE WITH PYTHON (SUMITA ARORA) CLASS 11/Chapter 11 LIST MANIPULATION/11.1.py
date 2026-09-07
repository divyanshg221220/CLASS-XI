#11.1
l=eval(input("Enter a list:"))
n=int(input("Enter the number:"))
for i in range(len(l)):
    l[i]+=n
print(l)