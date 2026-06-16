#7.6
def mymean(mylist):
    total=0
    count=0
    for i in mylist:
        total=total+i
        count=count+1
    mean=total/count
    print("The calculated mean is:",mean)
mylist=[1.3,2.4,3.5,6.9]
mymean(mylist)