#6.13
entry=0
sum1=0
print("enter numbers to find their sum, negative number ends the loop:")
while True:
    entry=int(input())
    if (entry<0):
        break
    sum1+=entry
print("Sum =", sum1)