# 39. Print a square number pattern using loops.
n = int(input("Enter size of squere :"))

for i in range(n):
    for j in range(1,n+1):
        print(j ,end=" ")
    print()