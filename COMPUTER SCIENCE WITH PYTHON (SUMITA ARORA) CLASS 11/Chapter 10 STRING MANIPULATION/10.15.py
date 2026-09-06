#10.15
s1=input("Enter a string:")
s2=""
l=s1.split(" ")
for i in l:
    s2+=i[::-1]
    s2+=" "
print(s2)