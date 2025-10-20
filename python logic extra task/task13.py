# 13. Find the factorial of a number using a loop.
num = int(input("Enter number to find factorial :"))

factorial = 1
for i in range(1,num+1):
    factorial = factorial * i

print(f"factorial of {num} is {factorial}")