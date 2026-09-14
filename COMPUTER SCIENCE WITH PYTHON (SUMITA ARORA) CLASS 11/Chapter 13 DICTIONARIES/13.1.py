#13.1
n=int(input("Enter number of employees:"))
d={}
for i in range(n):
    name=input("Enter name of employee:")
    salary=int(input("Enter salary of employee:"))
    d[name]=salary
print(d)