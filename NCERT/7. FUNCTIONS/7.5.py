#7.5
def incrValue(num):
    print("Parameter num has value:",num, "\nid =",id(num))
    num=num+5
    print("num incremented by 5 is",num,"\nNow id is ",id(num))
number=int(input("Enter a number: "))
print("id of argument number is:",id(number))
incrValue(number)