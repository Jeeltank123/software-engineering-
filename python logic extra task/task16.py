# 16. Count how many digits are in a given number.
num =  int(input("Enter num :"))
count = 0

while num > 0 :
    num =  num // 10
    count+=1
print("Total digit is",count)
