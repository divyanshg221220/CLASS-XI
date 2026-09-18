#14.4
l=eval(input("Enter a list of strings:"))
for i in range(1,len(l)):
    key=l[i]
    length=len(l[i])
    j=i-1
    while j>=0 and len(l[j])>length:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)