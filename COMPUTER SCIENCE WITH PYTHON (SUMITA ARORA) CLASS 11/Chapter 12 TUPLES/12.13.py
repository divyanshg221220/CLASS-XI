#12.13
t=eval(input("Enter a tuple:"))
count={}
for i in t:
    count[i]=count.get(i,0)+1
print(max(count,key=count.get))