#6.12
num=0
for num in range(10):
    num+=1
    if num == 8:
        break
    print("num has value"+str(num))
print('encountered break!! out of loop')