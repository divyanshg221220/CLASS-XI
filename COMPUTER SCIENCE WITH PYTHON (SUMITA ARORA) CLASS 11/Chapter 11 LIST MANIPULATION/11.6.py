#11.6
l=eval(input("Enter a list:"))
n=int(input("Enter the number:"))
if l.count(n):
    print("Present:",l.index(n))
else:
    print("Not present")