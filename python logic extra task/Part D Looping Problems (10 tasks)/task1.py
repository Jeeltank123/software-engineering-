# 31. Print Fibonacci series up to N terms.
N = int(input("Enter term :"))
A = 0
B = 1
temp = 0

for i in range(1,N+1):
# while N > 0 :
    print(A)
    temp = A+B
    A =  B
    B = temp

    # N=N-1