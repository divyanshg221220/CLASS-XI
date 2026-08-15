#9.20
while True:
    print("1. 2/9 - 5/13 + 8/17 ....... (print 7 terms)")
    print("2. 1^2 + 3^2 + 5^2 + ..... + n^2 (Input n)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    s=0
    if choice==1:
        for i in range(7):
            numerator=2+i*3
            denominator=9+i*4
            if i%2==0:
                s+=numerator/denominator
            else:
                s-=numerator/denominator
    elif choice==2:
        n=int(input("Enter a number:"))
        for i in range(1,n+1,2):
            s+=i**2
    elif choice==3:
        print("EXITED BY USER")
        break
    print("Sum:",s)
    print()