#12.6
t=tuple()
for i in range(5):
    print("Enter details of student",i+1)
    m1=float(input("Enter first subject marks:"))
    m2=float(input("Enter second subject marks:"))
    m3=float(input("Enter third subject marks:"))
    t+=(m1,m2,m3),
for i in range(5):
    m=0
    for j in range(3):
        m+=t[i][j]
    print("Total marks of student",i+1,":",m)
    print("Average marks of student",i+1,":",m/3)