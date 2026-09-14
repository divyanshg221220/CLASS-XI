#13.5
d={}
while True:
    name=input("Enter product name:")
    price=float(input("Enter product price:"))
    d[name]=price
    choice=input("Do you want to enter another product?(Y/N):")
    if choice.upper()=="N":
        break
while True:
    name=input("Enter product name:")
    if name in d:
        print("Price:",d[name])
    else:
        print("Product not in dictionary")
    choice=input("Do you want to search for another product?(Y/N):")
    if choice.upper()=="N":
        break