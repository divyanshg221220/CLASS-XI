#9.9
n=int(input("Enter a number:"))
l=[]
i=1
while len(l)!=n:
    if i%2!=0:
        l.append(i)
    i+=1
print("First n odd numbers in descending order:",l[::-1])