#13.12
D1={'A':[1,2,3], 'B':[4,5,6]}
D2={}
for i in D1:
    D2[i]=sum(D1[i])        
print("D2 is",D2)