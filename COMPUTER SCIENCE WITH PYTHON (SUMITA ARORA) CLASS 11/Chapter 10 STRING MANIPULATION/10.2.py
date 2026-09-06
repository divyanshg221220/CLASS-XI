#10.2
s=input("Enter a string:")
for i in s:
    if i in "aeiouAEIOU":
        print("*",end="")
    else:
        print(i,end="")