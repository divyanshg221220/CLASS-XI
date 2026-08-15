#9.17
l=eval(input("Enter a list:"))
for i in l:
    if str(i)==str(i)[::-1]:
        print(i)