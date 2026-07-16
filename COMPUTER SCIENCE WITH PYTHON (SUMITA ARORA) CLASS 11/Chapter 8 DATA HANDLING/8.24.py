p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time:"))
print("Compound interest:",p*(1+r/100)**t-p)