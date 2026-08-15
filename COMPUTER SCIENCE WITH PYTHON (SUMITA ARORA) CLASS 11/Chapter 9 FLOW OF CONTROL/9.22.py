#9.22
n=int(input("Enter a number:"))
l=[]
for i in range(n):
    l.append(int(input("Enter age of employee:")))
d={"26-25":0,"36-45":0,"46-55":0}
for i in l:
    if i>=25 and i<=35:
        d["26-25"]+=1
    elif i>=36 and i<=45:
        d["36-45"]+=1
    elif i>=46 and i<=55:
        d["46-55"]+=1
print("26-35:",d["26-25"])
print("36-45:",d["36-45"])
print("46-55:",d["46-55"])