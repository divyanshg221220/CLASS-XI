#9.21
n=int(input("Enter a number:"))
s=1
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f*=j
    s+=1/f
print("Sum:",s)