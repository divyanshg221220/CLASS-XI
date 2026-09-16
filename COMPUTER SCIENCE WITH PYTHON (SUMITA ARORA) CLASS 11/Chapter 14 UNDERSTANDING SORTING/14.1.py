#14.1
Election=eval(input("Enter a dictionary:"))
ListA=[]
ListB=[]
for i in Election:
    ListA.append(i)
    ListB.append(Election[i])
l=sorted(Election,key=Election.get,reverse=True)
for i in l:
    print(ListA[ListB.index(Election[i])])