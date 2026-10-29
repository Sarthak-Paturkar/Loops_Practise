##Find the largest digit in the given number
n = int(input("Any digit: "))
largest = n % 10
while n>0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10
print("largest digit",largest)