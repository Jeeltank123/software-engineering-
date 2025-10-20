# 27. Calculate electricity bill using slab system.
unit = int(input('Enter unit :'))
bill = 0

if unit <=50:
    bill = unit * 0.5

elif unit <= 150:
    bill = unit * 50 +((unit - 50 )*1)

elif unit <=250:
    bill = 50 * 50 + 100 * 1 + ((unit - 150 )*1.5)

else:
    bill = 50*50 + 100*1 + 100*1.5 + ((unit - 250 )*2 )

charges = bill * 0.5
total_bill = bill + charges

print(f"Total electicity bill :{total_bill}")