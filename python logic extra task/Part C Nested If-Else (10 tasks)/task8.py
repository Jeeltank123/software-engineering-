# 29. Find whether a triangle is scalene, isosceles, or equilateral.
side1 = int(input("Enter first side :"))
side2 = int(input("Enter second side :"))
side3 = int(input("Enter third side :"))

if (side1 + side2 > side3) and (side2 +side3 > side1) and (side1 + side3 > side2) :
    if side1 == side2 and side2 == side3 :
        print("equilateral triangle")

    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("isosceles tringle")
    else :
        print("scalene tringle")

else :
    print("not velid tringle")