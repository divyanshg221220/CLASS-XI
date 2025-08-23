#9.5
def linearSearch(num, list1):
    for i in range(0, len(list1)):
        if list1[i]==num:
            return i
    return None
list1=[]
print("How many numbers do you want to enter in the list: ")
maximum=int(input())
print("Enter the list of numbers: ")
for i in range(0, maximum):
    n=int(input())
    list1.append(n)
num=int(input("Enter the number to be searched: "))
result=linearSearch(num,list1)
if result is None:
    print("Number",num,"is not present in the list")
else:
    print("Number",num,"is present at",result+1,"position")