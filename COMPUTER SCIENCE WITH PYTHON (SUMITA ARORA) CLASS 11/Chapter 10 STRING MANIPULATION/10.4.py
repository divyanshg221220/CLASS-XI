#10.4
s=input("Enter a string:")
if len(s)==12 and s[:3].isdigit() and s[4:7].isdigit() and s[8:].isdigit() and s[3]=="-" and s[7]=="-":
    print("Valid")
else:
    print("Not valid")