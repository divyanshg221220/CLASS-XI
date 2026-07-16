#8.17
import math
side1=float(input("Enter side 1:"))
side2=float(input("Enter side 2:"))
angle=float(input("Enter angle:"))
print("Side 3:",math.sqrt(side1**2+side2**2-2*side1*side2*math.cos(math.radians(90))))