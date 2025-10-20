# 9. Check whether a character is uppercase, lowercase, digit, or special symbol.
ch = input("enter charecter :")

if ch >='A' and ch <= 'Z':
    print('charecter is uppercase ')
elif ch >='a' and ch <= 'z':
    print('charecter is lowercase')
elif ch >='0' and ch <='9':
    print('charecter is digit')
else:
    print('charecter is special symbol')
