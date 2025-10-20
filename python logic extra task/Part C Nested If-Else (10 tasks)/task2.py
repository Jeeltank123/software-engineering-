# 22. Find the largest of three numbers using nested if
A = int(input("Enter first number A  :"))
B = int(input("Enter second number B :"))
C = int(input("Enter third number C  :"))

if A > B:
    if A > C:
        print("A is largest number")
    else:
        print("C is largest number")

else:
    if B > C:
        print("B is largest number")
    else:
        print("C is largest number")