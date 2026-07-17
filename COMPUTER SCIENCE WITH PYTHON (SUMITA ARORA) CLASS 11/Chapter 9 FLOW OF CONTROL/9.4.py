#9.4
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if abs(a-b)<=.001:
    print("Close")
else:
    print("Not close")