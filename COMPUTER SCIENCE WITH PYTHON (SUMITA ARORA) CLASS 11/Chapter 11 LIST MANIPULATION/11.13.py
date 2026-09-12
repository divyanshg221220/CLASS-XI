#11.13
l=eval(input("Enter a list:"))
i=int(input("Enter the starting index:"))
j=int(input("Enter the ending index:"))
max=l[i]
min=l[i]
for k in range(i,j+1):
    if l[k]>max:
        max=l[k]
    if l[k]<min:
        min=l[k]
print("Maximum:",max)
print("Minimum:",min)