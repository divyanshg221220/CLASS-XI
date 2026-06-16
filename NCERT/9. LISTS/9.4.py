#9.4
def computeAverage(list1,n):
    total=0
    for marks in list1:
        total=total+marks
    average=total/n
    return average
list1=[]
print("How many students marks you want to enter: ")
n=int(input())
for i in range(0,n):
    print("Enter marks of student",(i+1),":")
    marks=int(input())
    list1.append(marks)
average=computeAverage(list1,n)
print("Average marks of",n,"students is:",average)
