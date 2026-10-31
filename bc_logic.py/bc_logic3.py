##Take 5 numbers as input, skip any number that is 0 using `continue`, and calculate the sum of the remaining numbers.
total = 0
for i in range(1,6):
    num = int(input("Enter a number:"))
    if num==0:
        continue
    total+=num
print(total)