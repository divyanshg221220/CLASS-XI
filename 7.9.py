#7.9
def mixedFraction(num,deno=1):
    remainder=num%deno
    if remainder!=0:
        quotient=int(num/deno)
        print("The mixed fraction=",quotient,"(",remainder,"/",deno,")")
    else:
        print("The given fraction evaluates to a whole number")
num=int(input("Enter the numerator: "))
deno=int(input("Enter the denominator: "))
print("You entered:",num,"/",deno)
if num>deno:
    mixedFraction(num,deno)
else:
    print("It is a proper fraction")