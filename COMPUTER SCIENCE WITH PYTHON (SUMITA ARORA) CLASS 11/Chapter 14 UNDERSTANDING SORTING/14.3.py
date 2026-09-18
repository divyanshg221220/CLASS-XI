#14.3
l=eval(input("Enter a list of 3-digit integers:"))
for i in range(1,len(l)):
    key=l[i]
    onesdigit=int(str(l[i])[-1])
    j=i-1
    while j>=0 and int(str(l[j])[-1])>onesdigit:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)