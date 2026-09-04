#9.24
while True:
    print("""1.
  *
 * *
* * *
 * *
  *""")
    print("""2.
*
* *
* * *
* *
*""")
    print("""3.
  *
 * *
*   *
 * *
  *""")
    print("""4.
*
* *
*   *
*     *
*   *
* *
*""")
    print("5. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        for i in range(1,4):
            print(" "*(3-i)+"*"+" *"*(i-1))
        for i in range(2,0,-1):
            print(" "*(3-i)+"*"+" *"*(i-1))
    elif choice==2:
        for i in range(1,4):
            print("*"+" *"*(i-1))
        for i in range(2,0,-1):
            print("*"+" *"*(i-1))
    elif choice==3:
        for i in range(1,4):
            print(" "*(3-i)+"*"+" "*(2*i-3)+"*"*(i>1))
        for i in range(2,0,-1):
            print(" "*(3-i)+"*"+" "*(2*i-3)+"*"*(i>1))
    elif choice==4:
        for i in range(1,5):
            print("*"+" "*(2*i-3)+"*"*(i>1))
        for i in range(3,0,-1):
            print("*"+" "*(2*i-3)+"*"*(i>1))
    elif choice==5:
        print("EXITED BY USER")
        break
    print()