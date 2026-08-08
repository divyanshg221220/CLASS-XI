#9.14
N=int(input("Enter a number (N > 20):"))
if N>20:
    for i in range(11,N+1):
        print(i,end=" ")
        if i%3==0 and i%7==0:
            print("Tipsy Topsy",end="")
        elif i%3==0:
            print("Tipsy",end="")
        elif i%7==0:
            print("Topsy",end="")
        print()