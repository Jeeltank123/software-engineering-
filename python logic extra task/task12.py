# 12. Print the sum of first N natural numbers.
n = int(input("Enter number : "))
sum = 0
for i in range (1,n+1):
    sum+=i
print("Sum is: ",sum)