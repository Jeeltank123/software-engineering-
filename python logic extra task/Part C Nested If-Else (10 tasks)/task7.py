# 28. Check if a person is child, teenager, adult, or senior citizen.
age = int(input("Enter person's age :"))

if age <=12:
    print("Person is a child")
elif age <=18 :
    print("Person is a teenager")
elif age <= 59:
    print("Person is an adult")
else :
    print("Person is senior citizen")