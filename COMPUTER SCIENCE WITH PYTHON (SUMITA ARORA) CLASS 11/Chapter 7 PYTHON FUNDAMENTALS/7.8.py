#7.8
h=float(input("Enter height in centimeters:"))
i=h/2.54
f=int(i//12)
i%=12
print("Feet:",f,"Inches:",i)