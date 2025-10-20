# 46. Count how many words, digits, and special characters in a string.
str = input("Enter string :")

words=0
digit = 0
s_ch = 0

for i in range(0,len(str)):

    if str[i] >= 'A' and str[i] <= 'Z':
        words+=1
    
    elif str[i] >= 'a' and str[i] <= 'z':
        words+=1
    
    elif str[i] >= '0' and str[i] <= '9' :
        digit+=1
    
    else:
        s_ch+=1

print("Total words :",words)
print("Total digit :",digit)
print("Total special characters :",s_ch)
