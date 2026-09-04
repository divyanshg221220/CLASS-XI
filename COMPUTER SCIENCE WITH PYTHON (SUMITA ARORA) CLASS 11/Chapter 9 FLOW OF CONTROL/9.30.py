#9.30
def prime_factors(n):
    factors=[]
    for i in range(2,n+1):
        while n%i==0:
            factors.append(i)
            n//=i
    return factors
n=int(input("Enter the maximum value to display: "))
for i in range(1,n+1):
    if i==1:
        print("1 = 1")
    else:
        factors=prime_factors(i)
        if len(factors)==1:
            print(f"{i} = {factors[0]} (prime)")
        else:
            print(f"{i} = " + "×".join(str(f) for f in factors))