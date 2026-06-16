#7.4
def sumSquares(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("The sum of first",n,"natural number is: ",sum)
num=int(input("Enter the value for n: "))
sumSquares(num)