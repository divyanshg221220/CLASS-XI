#10.6
line=[]
while True:
    s=input("Enter a sentence(s) folloed by \"enter\":")
    if s=="":
        break
    line.append(s)
s="\n".join(line)
print("original sentence(s):",s)
w=len(s.split())
c=len(s)
p=0
for i in s:
    if i.isalnum():
        p+=1
p=(p/c)*100
print("Number of words:",w)
print("Number of characters:",c)
print("Percentage of alphanumeric:",p)