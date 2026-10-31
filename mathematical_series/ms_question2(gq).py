##Find and print the **sum of the first n even numbers**.
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += 2 * i

print("Sum:", total)