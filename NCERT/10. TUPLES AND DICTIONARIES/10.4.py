#10.4
numbers=tuple()
n=int(input("How many numbers you want to enter?: "))
for i in range(0,n):
    num=int(input())
    numbers=numbers+(num,)
print('\nThe numbers in the tuple are:')
print(numbers)
print("\nThe maximum number is:")
print(max(numbers))
print("\nThe minimum number is:")
print(min(numbers))