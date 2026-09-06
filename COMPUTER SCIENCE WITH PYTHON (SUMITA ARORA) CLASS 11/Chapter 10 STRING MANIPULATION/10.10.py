#10.10
n=int(input("Enter an integer:"))
ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
hundreds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
thousands=["","M","MM","MMM"]
thousands_digit=n//1000
hundreds_digit=(n%1000)//100
tens_digit=(n%100)//10
ones_digit=n%10
r=thousands[thousands_digit]+hundreds[hundreds_digit]+tens[tens_digit]+ones[ones_digit]
print(n,"=",r)