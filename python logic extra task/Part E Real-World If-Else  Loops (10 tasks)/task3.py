# 43. Ticket price calculation with age-based discount.
t_price =200

age = int(input("Enter your age :"))

if age <= 5 :
    discount = 100

elif age <=12 :
    discount = 50

elif age <=55 :
    discount = 15
elif age > 55 :
    discount = 30

f_price = t_price - t_price * discount / 100 

print("Ticket price :",t_price)
print(f"Total discount :{discount}%")
print("Final price :",f_price)