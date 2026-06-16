#8.2
def replaceVowel(st):
    newstr=''
    for character in st:
        if character in 'aeiouAEIOU':
            newstr+='*'
        else:
            newstr+=character
    return newstr
st=input("Enter a string: ")
st1=replaceVowel(st)
print("The original string is:",st)
print("The modified string is:",st1)