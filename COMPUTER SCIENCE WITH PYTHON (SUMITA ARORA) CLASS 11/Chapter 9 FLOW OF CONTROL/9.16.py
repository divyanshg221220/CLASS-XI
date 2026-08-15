#9.16
N=int(input("Enter the number:"))
l=[]
for i in range(N):
    l.append(int(input("Enter the number:")))
l.sort()
print("Second largest number:",l[-2])