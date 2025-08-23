#10.3
def circle(r):
    area=3.14*r*r
    circumference=2*3.14*r
    return(area,circumference)
radius=int(input("Enter radius of circle: "))
area,circumference=circle(radius)
print('Area of circle is:',area)
print('Circumference of circle is:',circumference)
