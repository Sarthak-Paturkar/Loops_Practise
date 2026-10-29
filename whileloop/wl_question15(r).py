##Check whether the given number is an Armstrong number
n = int(input("Enter a number: "))
original = n
temp = n
count = 0
total = 0

# Count the number of digits
while temp != 0:
    count += 1
    temp = temp // 10

# Calculate the sum of powered digits
temp = n

while temp != 0:
    digit = temp % 10
    total += digit ** count
    temp = temp // 10

# Check whether it is an Armstrong number
if total == original:
    print("It's an Armstrong number")
else:
    print("It's not an Armstrong number")