# 40. Generate a half pyramid with numbers.
n = int(input("Enter half pyramid lenth :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()