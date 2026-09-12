#11.11
while True:
    print('''1. Print the length of the longest
string in the list of strings str_list.
Precondition : the list will contain
at least one element.''')
    print('''2. L is a list of numbers. Print a new list where each element is the
corresponding element of list L summed with number num.''')
    print("3. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        str_list=eval(input("Enter a list of strings:"))
        max=len(str_list[0])
        for i in str_list:
            if len(i)>max:
                max=len(i)
        print(max)
    elif choice==2:
        L=eval(input("Enter a list of numbers:"))
        num=int(input("Enter the number:"))
        l=[]
        for i in L:
            l.append(i+num)
        print(l)
    elif choice==3:
        print("EXITED BY USER")
        break
    print()