#7.11
p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time:"))
print("Simple interest:",(p*r*t)/100)
print("Compound interest:",p*(1+r/100)**t-p)