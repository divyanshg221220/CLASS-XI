#7.15
num=5
def myfunc1():
    global num
    print("Accessing num=",num)
    num=10
    print("num reassigned=",num)
myfunc1()
print("Accessing num outside myfunc1",num)