#10.8
while True:
    integer_input=int(input("Enter an integer:"))
    s=input("Enter a string:")
    string_digit="0"
    for i in s:
        if i.isdigit():
            string_digit+=i
    string_digit=int(string_digit)
    print("For inputs",integer_input,", '",s,"'-> '",integer_input,"+",string_digit,"=",integer_input+string_digit,"'")