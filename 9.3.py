#9.3
myList=[22,4,16,38,13]
choice=0
while True:
    print("The list 'myList' has the following elements", myList)
    print("\nLIST OPERATIONS")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element by its position")
    print("6. Delete an existing element by its value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")
    choice=int(input("ENTER YOUR CHOICE (1-10): "))
    if choice==1:
        element=int(input("Enter the element to be appended:"))
        myList.append(element)
        print("The element has been appended\n")
    elif choice == 2:
        element = int(input("Enter the element to be inserted: "))
        pos = int(input("Enter the position:"))
        myList.insert(pos,element)
        print("The element has been inserted\n")
    elif choice == 3:
        newList = eval(input("Enter the elements separated by commas: "))
        myList.extend(list(newList))
        print("The list has been appended\n")
    elif choice == 4:
        i = int(input("Enter the position of the element to be modified: "))
        if i < len(myList):
            newElement = int(input("Enter the new element: "))
            oldElement = myList[i]
            myList[i] = newElement
            print("The element",oldElement,"has been modified\n")
        else:
            print("Position of the element is more than the length of list")
    elif choice == 5:
        i = int(input("Enter the position of the element to be deleted: "))
        if i < len(myList):
            element = myList.pop(i)
            print("The element",element,"has been deleted\n")
        else:
            print("Position of the element is more than the length of list")
    elif choice == 6:
        element = int(input("Enter the element to be deleted: "))
        if element in myList:
            myList.remove(element)
            print("\nThe element",element,"has been deleted\n")
        else:
            print("\nElement",element,"is not present in the list")
    #list in sorted order
    elif choice==7:
        myList.sort()
        print("\nThe list has been sorted")
    elif choice==8:
        myList.sort(reverse=True)
        print("\nThe list has been sorted in reverse order")
    elif choice==10:
        break