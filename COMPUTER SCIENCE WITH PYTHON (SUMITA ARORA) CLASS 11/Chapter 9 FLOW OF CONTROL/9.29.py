#9.29
t=float(input("Enter temperature in celsius:"))
if t<-273.15:
    print("temperature is invalid because it is below absolute zero.")
elif t==-273.15:
    print("temperature is absolute 0.")
elif t>-273.15 and t<0:
    print("temperature is below freezing.")
elif t==0:
    print("temperature is at the freezing point.")
elif t>0 and t<100:
    print("temperature is in the normal range.")
elif t==100:
    print("temperature is at the boiling point.")
elif t>100:
    print("temperature is above the boiling point.")