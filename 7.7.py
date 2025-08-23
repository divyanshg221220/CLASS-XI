#7.7
def calcFact(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    print("Factorial of",num,"is",fact)
num=int(input("Enter the number: "))
calcFact(num)