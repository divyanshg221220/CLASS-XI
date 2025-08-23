#7.14
num=5
def myFunc1():
    y=num+5
    print("Accessing num-> (global) in myFunc1,value=",num)
    print("Accessing y-> (local variable of myFunc1) accessible, value=",y)
myFunc1()
print("Accessing num outside myFunc1 ",num)
print("Accessing y outside myFunc1 ",y)
