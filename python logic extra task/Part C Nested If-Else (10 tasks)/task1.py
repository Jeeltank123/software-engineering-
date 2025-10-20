# 21. Input marks and print grade (A, B, C, D, Fail).
marks = int(input('Enter marks :'))

if marks >85:
    print("student grade is A")
elif  marks >75:
     print("student grade is B")
elif marks > 65:
     print("student grade is C")
elif marks > 35 :
     print("student grade is D")
else :
     print("student is fail")