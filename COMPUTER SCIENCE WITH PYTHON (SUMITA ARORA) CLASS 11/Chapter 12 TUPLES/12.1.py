#12.1
t=(0,1)
for i in range(2,9):
    t+=(t[i-1]+t[i-2],)
print(t)