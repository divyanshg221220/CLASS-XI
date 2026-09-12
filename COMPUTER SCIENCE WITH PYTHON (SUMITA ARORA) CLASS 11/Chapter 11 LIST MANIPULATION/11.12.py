#11.12
num=eval(input("Enter a list of numerators:"))
denum=eval(input("Enter a list of denominators:"))
min=num[0]/denum[0]
index=0
for i in range(len(num)):
    if num[i]/denum[i]<min:
        min=num[i]/denum[i]
        index=i
print(num[index],"/",denum[index],"=",min)