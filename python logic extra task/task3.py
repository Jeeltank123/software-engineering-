# 3. Check whether a given year is a leap year or not.
year = int(input("Enter year : "))

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")