# 17. Reverse the digits of a number using a loop.
num  = int(input("Enter num :"))
rim = 0
reverce = 0

while num > 0:
    rim = num % 10
    reverce = reverce * 10 + rim
    num = num // 10

print("Reverce num :",reverce)
