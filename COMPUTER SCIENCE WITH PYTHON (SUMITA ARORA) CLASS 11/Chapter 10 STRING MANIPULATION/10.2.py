#10.2
s=input("Enter a string:")
for i in s:
    if i in "aeiou":
        print("*",end="")
    else:
        print(i,end="")