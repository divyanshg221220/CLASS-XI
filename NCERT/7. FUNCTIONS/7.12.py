#7.12
def calcAreaPeri(length,breadth):
    area=length*breadth
    perimeter=2*(length+breadth)
    return (area,perimeter)
l=float(input("Enter length of the rectangle: "))
b=float(input("Enter breadth of the rectangle: "))
area,perimeter=calcAreaPeri(l,b)
print("Area is:",area,"\nPerimeter is:",perimeter)