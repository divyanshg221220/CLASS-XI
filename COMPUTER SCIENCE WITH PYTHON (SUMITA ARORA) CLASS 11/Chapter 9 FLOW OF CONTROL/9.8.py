#9.8
import math
n=int(input("Enter a number:"))
sqrt=math.sqrt(n)
if sqrt==int(sqrt):
    if sqrt<2:
        print("Not prime")
    else:
        for i in range(2,int(math.sqrt(sqrt))+1):
            if sqrt%i==0:
                print("Not prime")
                break
        else:
            print("Prime")
else:
    print("Not prime")