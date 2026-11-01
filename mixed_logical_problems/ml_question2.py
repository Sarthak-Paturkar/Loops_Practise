##Count total numbers between 1 & 1000 that are divisible by 7 but not divisible by 5
count = 0
for i in range(1,1001):
    if i % 7 == 0 and i % 5 != 0:
        count+=1
        print(i)
print()
print("Total count:", count)