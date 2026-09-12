#11.7
while True:
    print("1. A list consisting of the integers 0 through 49.")
    print("2. A list containing the squares of the integers 1 through 50.")
    print("3. The list ['a','bb','ccc','dddd', ... ] that ends with 26 copies of the letter z.")
    print("4. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        l=list(range(50))
        print(l)
    elif choice==2:
        l=[i**2 for i in range(1,51)]
        print(l)
    elif choice==3:
        l=[chr(97+i)*(i+1) for i in range(26)]
        print(l)
    elif choice==4:
        print("EXITED BY USER")
        break
    print()