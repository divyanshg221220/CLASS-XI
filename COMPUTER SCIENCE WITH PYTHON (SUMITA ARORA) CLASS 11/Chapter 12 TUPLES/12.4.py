#12.4
from unicodedata import name
n=int(input("Enter the number:"))
t=tuple()
for i in range(n):
    rollnumber=int(input("Enter the roll number:"))
    name=input("Enter the name:")
    marks=float(input("Enter the marks:"))
    t+=(rollnumber,name,marks),
print(t)