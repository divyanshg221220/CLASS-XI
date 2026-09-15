#13.8
x={'k1':'v1','k2':'v2','k3':'v3'}
inverted_x={}
for i in x:
    inverted_x[x[i]]=i
print("inverted_x =",inverted_x)