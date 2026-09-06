#10.9
s1=input("Enter first string: ")
s2=input("Enter second string: ")
if len(s1)<=len(s2):
    smaller,larger=s1,s2
else:
    smaller,larger=s2,s1
print(smaller)
n=len(larger)
for i in range((n+1)//2):
    right_index=n-1-i
    if i==right_index:
        print(" "*i+larger[i])
    else:
        print(" "*i+larger[i]+" "*(right_index-i-1)+larger[right_index])