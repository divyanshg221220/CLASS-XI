#9.25
while True:
    print("""1.
A
A B
A B C
A B C D
A B C D E
A B C D E F
""")
    print("""2.
A
B B
C C C
D D D D
E E E E E""")
    print("""3.
0
2 2
4 4 4
6 6 6 6
8 8 8 8 8""")
    print("""4.
2
4 4
6 6 6
8 8 8 8""")
    print("5. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        for i in range(1,7):
            for j in range(65,65+i):
                print(chr(j),end=" ")
            print()
    elif choice==2:
        for i in range(0,5):
            for j in range(0,i+1):
                print(chr(65+i),end=" ")
            print()
    elif choice==3:
        for i in range(0,5):
            for j in range(0,i+1):
                print(i*2,end=" ")
            print()
    elif choice==4:
        for i in range(1,5):
            for j in range(0,i):
                print(i*2,end=" ")
            print()
    elif choice==5:
        print("EXITED BY USER")
        break
    print()