##Find and print the **sum of the first n odd numbers**.
##Find and print the **sum of the first n even numbers**.
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += 2 * i - 1

print("Sum:", total)