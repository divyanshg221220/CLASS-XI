#12.9
while True:
    print("1. A tuple containing the squares of the integers 1 through 50.")
    print("2. The tuple ('a', 'bb', 'ccc', 'dddd', ... ) that ends with 26 copies of the letter z.")
    print("3. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        t=tuple(i**2 for i in range(1,51))
        print(t)
    elif choice==2:
        t=tuple(chr(97+i)*(i+1) for i in range(26))
        print(t)
    elif choice==3:
        break
    print()