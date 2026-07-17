#9.3
t=int(input("Enter hours between 1-12 : "))
h=int(input("How many hours ahead : "))
t+=h
if t>12:
    t-=12
print("Time at that time would be :",t,"0'clock")