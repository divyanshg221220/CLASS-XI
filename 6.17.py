#6.17
num=int(input("Enter a number to generate its pattern = "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
