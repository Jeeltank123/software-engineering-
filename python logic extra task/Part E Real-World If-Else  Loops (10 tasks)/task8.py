# 50. Print the multiplication table from 1 to 10 using nested loops.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()