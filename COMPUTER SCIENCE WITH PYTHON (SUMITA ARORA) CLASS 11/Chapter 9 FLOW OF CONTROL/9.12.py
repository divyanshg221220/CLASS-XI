#9.12
side1=float(input("Enter side 1:"))
side2=float(input("Enter side 2:"))
side3=float(input("Enter side 3:"))
if side1==side2==side3:
    print("Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")