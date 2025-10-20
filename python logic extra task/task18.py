# 18. Check whether a number is a palindrome (e.g., 121 → palindrome).
num = int(input("Enter num to find palindrome :"))
org = num
reverce = 0
rim = 0

while num > 0:
    rim = num % 10
    reverce = reverce * 10 + rim
    num = num // 10

if org == reverce:
    print(f"{org} is pelindrome number")
else :
    print(f"{org} is not pelindrome number")