#8.2
l=[]
d=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(7):
    l.append(float(input("Enter temperature of "+str(d[i])+":")))
print("Average:",sum(l)/len(l))