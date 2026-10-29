##Find the smallest digit in the given number
n = int(input("Any digit: "))
smallest = n % 10
while n>0:
    digit = n% 10
    if digit < smallest:
        smallest = digit
    n = n // 10

print("Smallest digit",smallest)