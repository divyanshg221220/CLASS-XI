#12.10
pairs=((2,5),(4,2),(9,8),(12,10))
count=0
for a,b in pairs:
    if a%2==0 and b%2==0:
        count+=1
print(count)