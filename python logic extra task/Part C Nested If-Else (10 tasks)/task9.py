# 30. Find whether roots of quadratic equation are real, equal, or imaginary.
a = float(input("Enter velue of A :"))
b = float(input("Enter velue of B :"))
c = float(input("Enter velue of C :"))

d = (b * b) - (4 * a * c)

if d < 0:
    print("roots are real and distinct")
elif d == 0:
    print("roots are real and equal")
else :
    print("numbers are imaginary")

