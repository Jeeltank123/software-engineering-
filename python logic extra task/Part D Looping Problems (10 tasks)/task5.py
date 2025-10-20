# 35. Check whether a number is prime.
num = int(input("Enter Number :"))

if num > 1:
    for i in range (2,num):
        if num % i == 0:
            print("Number is Not prime:")
            break
    else:
            print("Number is prime")

else:
     print("Number is not prime (should be greater than 1)")