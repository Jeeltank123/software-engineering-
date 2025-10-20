# 36. Print the sum of digits of a number.
num = int(input("Enter number :"))
sum = 0 
while num > 0:
    rim =num % 10
    sum+=rim
    num= num//10
print("Sum of digit is :",sum)