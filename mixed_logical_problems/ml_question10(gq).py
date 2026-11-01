##Find the number between 1 and n that has the maximum digit sum, and print that number along with its digit sum
n = int(input("Enter n: "))

max_sum = 0
max_num = 0

for i in range(1, n + 1):
    temp = i
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = i

print("Number:", max_num)
print("Maximum digit sum:", max_sum)