#13.7
d={}
for i in range(10):
    rollno=int(input("Enter roll number:"))
    name=input("Enter name:")
    marks=float(input("Enter marks:"))
    grade=input("Enter grade:")
    d[i+1]={"rollno":rollno,"name":name,"marks":marks,"grade":grade}
print(d)