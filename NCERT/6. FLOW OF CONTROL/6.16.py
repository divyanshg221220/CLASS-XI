#6.16
for var1 in range(3):
    print("Iteration "+str(var1+1)+" of outer loop")
    for var2 in range(2):
        print(var2+1)
    print("Out of inner loop")
print("Out of outer loop")