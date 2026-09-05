#10.5
s=input("given the input :")
d=""
sum=0
f=0
for i in s:
    if i.isdigit():
        d+=i
        sum+=int(i)
        f=1
if f==1:
    print(s,"has the digits",d,"which sum to",sum)
else:
    print(s,"has no digits")