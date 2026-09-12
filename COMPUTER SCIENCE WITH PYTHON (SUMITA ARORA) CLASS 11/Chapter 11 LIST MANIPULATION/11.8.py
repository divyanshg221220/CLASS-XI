#11.8
L=eval(input("Enter first list:"))
M=eval(input("Enter second list:"))
N=[]
for i in range(len(L)):
    N.append(L[i]+M[i])
print(N)