#12.2
while True:
    print("1. Write a program that recives the index and return the corresponding value.")
    print("2. Write a program that receives a Fibonacci term and returns a number telling which term it is. For instance, if you pass 3, it returns 5, telling it it 5th term; for 8, it returns 7.")
    print("3. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        t=eval(input("Enter a tuple:"))
        index=int(input("Enter the index:"))
        print(t[index])
    elif choice==2:
        n=int(input("Enter a Fibonacci term:"))
        t=(0,1)
        for i in range(2,100):
            t+=(t[i-1]+t[i-2],)
            if n==t[i]:
                print(i+1)
                break
    elif choice==3:
        print("EXITED BY USER")
        break
    print()