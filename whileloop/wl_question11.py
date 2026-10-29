##Count and print the total number of digits in a given number
n = int(input("Enter a digit: "))
count = 0
while n!=0:
    digit = n % 10
    count = count + 1
    n = n // 10
print(count)