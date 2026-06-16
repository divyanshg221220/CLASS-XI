#8.4
def reverseString(st):
    newstr=''
    length=len(st)
    for i in range(-1,-length-1,-1):
        newstr+=st[i]
    return newstr
st=input("Enter a String: ")
st1=reverseString(st)
print("The original string is:",st)
print("The reversed string is:",st1)
