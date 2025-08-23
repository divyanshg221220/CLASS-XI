#7.10
def calcpow(number,power):  
     result=1
     for i in range(1,power+1):
          result=result*number
     return result
base=int(input("Enter the value for the Base: "))
expo=int(input("Enter the value for the Exponent: "))
answer=calcpow(base,expo)
print(base,"raised to the power",expo,"is",answer)