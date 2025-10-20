# 20. Generate the multiplication table of a number.
num = int(input("enter num to generetes its multiplication table : "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")