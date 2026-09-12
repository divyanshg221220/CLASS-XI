#12.3
n=int(input("Enter the number:"))
t=tuple()
for i in range(n):
    t+=(int(input("Enter the number:")),)
print("Max:",max(t))
print("Min:",min(t))