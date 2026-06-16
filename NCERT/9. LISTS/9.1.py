#9.1
def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
    print('Reference of list Inside Function',id(list2))
list1=[10,20,30,40,50]
print("Reference of list in Main",id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)