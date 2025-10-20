# 23. Check whether a given number lies in a range [x, y].
X = int(input('Enter X line range :'))
Y = int(input('Enter Y line range :'))

N = int(input('Enter number to chek in range or not :'))

if N >= X and N <= Y:
    print("Number is in line ")
else :
    print("Number is out of line")