#9.27
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
l=[a,b,c]
l.sort()
print("Smallest number =",l[0])
print("Next higher number =",l[1])
print("Highest number =",l[2])