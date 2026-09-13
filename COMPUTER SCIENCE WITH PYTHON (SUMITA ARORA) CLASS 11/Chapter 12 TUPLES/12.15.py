#12.15
tup1=((1,2),(3,4.15,5.15),(7,8,12,15))
mean=tuple()
for i in range(len(tup1)):
    mean+=((sum(tup1[i])/len(tup1[i])),)
    print("Mean elements",i+1,":",mean[i],";")
print("Mean of means",sum(mean)/len(mean))