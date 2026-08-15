#9.19
n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%m==0:
        print(i,end=" ")
        if i%2==0:
            print("even")
        else:
            print("odd")