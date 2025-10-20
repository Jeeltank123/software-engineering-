# 45. Count how many students passed/failed in a list.
marks = [75, 42, 90, 33, 67, 28, 55, 80, 49, 60]
passed=0
faild=0
for i in range(0,10):
    mark = marks[i]

    if mark > 35:
        passed+=1
    else:
        faild+=1

print("Total passed student :",passed)
print("Total faild student :",faild)