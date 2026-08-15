#9.16
N=int(input("Enter a number:"))
l=[]
for i in range(N):
    l.append(int(input("Enter a number:")))
l.sort()
print("Second largest number:",l[-2])