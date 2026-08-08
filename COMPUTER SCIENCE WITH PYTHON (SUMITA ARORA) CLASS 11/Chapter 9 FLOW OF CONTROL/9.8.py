#9.8
import math
n=int(input("Enter a number:"))
sqrt=math.sqrt(n)
if sqrt==int(sqrt):
    if sqrt<2:
        print(sqrt,"is not a prime number")
    else:
        for i in range(2,int(math.sqrt(sqrt))+1):
            if sqrt%i==0:
                print(sqrt,"is not a prime number")
                break
        else:
            print(sqrt,"is a prime number")
else:
    print(sqrt,"is not a prime number")