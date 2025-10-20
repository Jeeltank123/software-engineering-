# 41. ATM machine: check PIN and balance withdrawal.
c_pin = 2509
balance = 50000.00

pin=int(input("Enter your pin :"))

if pin == c_pin:
    print("====WELCOME====")
    print("Your current balance is :",balance)

    withdraw = float(input("Enter withdrawal ammount :"))

    if withdraw > balance :
        print("Insufficient balance")

    elif withdraw <= 0:
        print("invelid ammount")

    else:
        balance = balance - withdraw

        print(f"Rupees {withdraw} has been successfuly withdrawan")
        print("Updated balance :",balance)