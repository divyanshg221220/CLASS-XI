#8.5
def checkPalin(st):
    i=0
    j=len(st)-1
    while(i<=j):
        if(st[i]!=st[j]):
            return False
        i+=1
        j-=1
    return True
st=input("Enter a String: ")
result=checkPalin(st)
if result==True:
    print("The given string",st,"is a palindrome")
else:
    print("The given string", st, "is not a palindrome")