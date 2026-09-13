#12.8
str_tuple=eval(input("Enter a tuple of strings: "))
min=str_tuple[0]
for i in range(len(str_tuple)):
    if len(str_tuple[i])<len(min):
        min=str_tuple[i]
print(len(min))