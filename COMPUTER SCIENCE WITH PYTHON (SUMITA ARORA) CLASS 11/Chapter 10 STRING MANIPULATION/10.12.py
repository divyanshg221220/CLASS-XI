#10.12
s=input("Enter a formula:")
o=0
c=0
for i in s:
    if i=="(":
        o+=1
    elif i==")":
        c+=1
if o==c:
    print("Same number of opening and closing parenthesis")
else:
    print("Different number of opening and closing parenthesis")