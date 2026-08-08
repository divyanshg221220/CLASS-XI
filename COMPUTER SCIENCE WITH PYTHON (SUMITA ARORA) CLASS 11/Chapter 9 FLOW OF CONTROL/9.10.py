#9.10
while True:
    print("1. 1    4    7    10 ...... 40.")
    print("2. 1   -4    7   -10 ......-40")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        for i in range(1,41,3):
            print(i,end="  ")
    elif choice==2:
        for i in range(1,41,3):
            if i%2==0:
                print(-i,end="  ")
            else:
                print(i,end="  ")
    elif choice==3:
        print("EXITED BY USER")
        break
    print()