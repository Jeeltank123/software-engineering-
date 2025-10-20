# 10. Check if three sides form a valid triangle.
a =int(input("enter first side :"))
b =int(input("enter second side:"))
c =int(input("enter third side:"))

if (a+b >c) and( b+c >a )and (c+a >b):
    print('It is valid triangle')
else:
    print('it is not valid')