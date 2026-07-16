#8.16
import random
s=0
l=[]
for i in range(6):
    r=random.random()
    print(r)
    s+=r
    l.append(r)
print("Mean:",s/6)
l=sorted(l)
mid=len(l)//2
print("Median:",(l[mid-1]+l[mid])/2)
max_count=0
mode=0
for i in l:
    count=l.count(i)
    if count>max_count:
        max_count=count
        mode=i
    elif count==max_count:
        mode=i
print("Mode:",mode)