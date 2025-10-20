# 32. Find the GCD (HCF) of two numbers using loops.
n1 = int(input("Enter first num :"))
n2 = int(input("Enter second num :"))

gcd = 1
i=1
while i<=n1 and i<=n2 :
    if(n1 % i == 0) and (n2 % i == 0):
        gcd = i
    
    i+=1
print("GCD (HCF) of two numbers :",gcd)