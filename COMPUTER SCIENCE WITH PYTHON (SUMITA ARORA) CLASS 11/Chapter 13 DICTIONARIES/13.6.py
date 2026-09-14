#13.6
d={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
while True:
    print("1. Ask the user to enter a month name and use the dictionary to tell how many days are in the month.")
    print("2. Print out all of the keys in alphabetical order.")
    print("3. Print out all of the months with 31 days.")
    print("4. Print out the (key-value) pairs sorted by the number of days in each month.")
    print("5. EXIT")
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        month=input("Enter month name:")
        print("Days:",d[month])
    elif choice==2:
        print("Months in alphabetical order:",sorted(d.keys()))
    elif choice==3:
        print("Months with 31 days:",[month for month in d if d[month]==31])
    elif choice==4:
        print("Months sorted by number of days:")
        for month in sorted(d,key=d.get):
            print(month,":",d[month])
    elif choice==5:
        print("EXITED BY USER")
        break
    print()        