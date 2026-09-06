#10.13
s=input("Enter a string:")
c=0
for i in s:
    if i in "aeiouAEIOU":
        c+=1
print(s)
print("Count of vowels:",c)