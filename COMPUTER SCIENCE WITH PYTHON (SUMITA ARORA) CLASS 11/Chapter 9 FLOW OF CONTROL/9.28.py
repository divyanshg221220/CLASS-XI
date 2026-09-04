#9.28
t=float(input("Enter temperature:"))
u=input("Enter unit (C/F):")
if u=='C':
    f=(t*9/5)+32
    print("Temperature in fahrenheit:",f)
elif u=='F':
    c=(t-32)*5/9
    print("Temperature in celsius:",c)