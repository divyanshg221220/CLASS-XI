#7.7
l=[]
for i in range(5):
    l.append(float(input("Enter marks of subject",i+1,":")))
print("Average:",sum(l)/len(l))