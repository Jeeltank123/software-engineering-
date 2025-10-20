# 6. Find the smallest of three numbers.
A = int(input("Enter A :"))
B = int(input('Enter B :'))
C = int(input("Enter C :"))

if A < B and A<C :
    print('A is smallest')
elif B < A and B < C:
    print('B is smallest')
else:
    print("C is smallest")
