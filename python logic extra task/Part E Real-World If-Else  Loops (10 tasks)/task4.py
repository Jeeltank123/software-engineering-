# 44. Shopping discount calculator (10% if bill > 1000).
bill = int(input("Enter total bill :"))

if bill < 1000:
    dis = 0 

elif bill >= 1000 and bill <5000 :
    dis = 10

elif bill >=5000 and bill <10000:
    dis = 15

else:
    dis = 20

d_bill = bill - bill * dis / 100 

print("Total Bill :",bill)
print(f"Total discount :{dis}%")
print("Final price :",d_bill)
