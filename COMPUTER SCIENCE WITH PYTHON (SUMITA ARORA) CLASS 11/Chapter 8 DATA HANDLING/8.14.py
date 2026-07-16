#8.14
import random
count=0
while count<3:
    r=random.randint(100,999)
    if r%5==0:
        print(r)
        count+=1