# 26. Print whether a given date (dd, mm, yyyy) is valid or not
dd=int(input("Enter day :"))
mm = int(input("Enter month :"))
yyyy=int(input("Enter year :"))

if mm >= 1 and mm <=12:
    if mm in [1,3,5,7,8,10,12]:
        if dd >= 1 and dd <=31 :
            print("velid date")
        else:
            print("invelid date")
    elif mm in [4,6,9,11]:
        if dd >=1 and dd<= 30:
            print("velid date")
        else:
            print("invelid date")
    elif mm == 2 :
        if yyyy % 4 == 0:
            if dd >= 1 and dd <=29:
                print("velid date")
            else:
                print("invelid date")
        elif yyyy % 4 != 0:
            if dd>=1 and dd<= 28 :
                print("velid date")
            else:
                print('invelid date')
else:
    print("invelid date")

