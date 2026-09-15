#13.10
D1={'a':10,'b':20,'c':10}
D2={'a':10,'b':20,'c':30}
d={}
for i in D1:
    if D1[i] not in d:
        d[D1[i]]=1
    else:
        d[D1[i]]+=1
for i in d:
    if d[i]>1:
        print(d[i],"keys have same values")
        break
else:
    print("No keys have same values")
d={}
for i in D2:
    if D2[i] not in d:
        d[D2[i]]=1
    else:
        d[D2[i]]+=1
for i in d:
    if d[i]>1:
        print(d[i],"keys have same values")
        break
else:
    print("No keys have same values")