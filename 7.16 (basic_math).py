#7.16
"""
basic math Module
********************
This module contains basic arithmetic operations
that can be carried out on numbers
"""
def addnum(x,y):
    return (x+y)
def subnum(x,y):
    return (x-y)
def multnum(x,y):
    return (x*y)
def divnum(x,y):
    if y==0:
        print("Division by Zero Error")
    else:
        return (x/y)
