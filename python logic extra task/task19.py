# 19. Check whether a number is an Armstrong number (e.g., 153 → 1³+5³+3³ = 153).
num = int(input("Enter num to find armstrong number :"))
org = num
arm = 0
rim = 0

count = len(str(num))
while num > 0:
    rim = num % 10
    arm = arm + rim ** count
    num = num // 10

if org == arm:
    print(f"{org} is armstrong num")
else:
    print(f"{org} is not armstrong num")