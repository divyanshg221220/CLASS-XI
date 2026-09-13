#12.5
marks=tuple()
for i in range(5):
    print("Enter details of student",i+1)
    m1=float(input("Enter first subject marks:"))
    m2=float(input("Enter second subject marks:"))
    m3=float(input("Enter third subject marks:"))
    marks+=(m1,m2,m3),
print("marks",marks)