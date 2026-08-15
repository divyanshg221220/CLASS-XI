#9.23
while True:
    print("1. x - x^2/2! + x^3/3! - x^4/4! + x^5/5! - x^6/6! (Input x)")
    print("2. x + x^2/2 + x^3/3 + ..... + x^n/n (Input x and n both)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    s=0
    if choice==1:
        x=int(input("Enter a number:"))
        for i in range(1,7):
            f=1
            for j in range(1,i+1):
                f*=j
            if i%2==0:
                s-=x**i/f
            else:
                s+=x**i/f
    elif choice==2:
        x=int(input("Enter a number:"))
        n=int(input("Enter a number:"))
        for i in range(1,n+1):
            s+=x**i/i
    elif choice==3:
        print("EXITED BY USER")
        break
    print("Sum:",s)
    print()