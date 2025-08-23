#7.2
def cyl(h,r):
    area_cyl=2*3.14*r*h
    return(area_cyl)
def con(l,r):
    area_con=3.14*r*l
    return (area_con)
def post_tax_price(cost):
    tax=0.18*cost
    net_price=cost+tax
    return(net_price)
print("Enter values for the cylindrical part of the tent in meters:")
h=float(input("Height: "))
r=float(input("Radius: "))
csa_cyl=cyl(h,r)
l=float(input("Enter the slant height of the conical area in meters:"))
csa_con=con(l,r)
canvas_area=csa_cyl+csa_con
print("The area of canvas = ",canvas_area,"m^2")
unit_price=float(input("Enter the cost of 1 m^2 canvas in rupees: "))
total_cost=unit_price*canvas_area
print("Total cost of canvas before tax = ",total_cost)
print("Net amount payable (including tax) = ",post_tax_price(total_cost))
