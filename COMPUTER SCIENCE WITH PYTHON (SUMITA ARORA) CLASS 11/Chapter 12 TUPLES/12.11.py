#12.11
seq_a=eval(input("Enter first tuple:"))
seq_b=eval(input("Enter second tuple:"))
for i in seq_a:
    if i not in seq_b:
        print(False)
        break
else:
    print(True)