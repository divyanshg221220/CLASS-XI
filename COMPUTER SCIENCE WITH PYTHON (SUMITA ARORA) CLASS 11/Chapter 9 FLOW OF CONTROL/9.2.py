#9.2
n=int(input("Enter number of items:"))
if n<10:
    print("Rs.",120*n)
elif n>=10 and n<=99:
    print("Rs.",100*n)
elif n>=100: 
    print("Rs.",70*n)