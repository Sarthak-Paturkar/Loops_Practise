##Calculate the sum of all even numbers from 1 up to n
n = int(input("Enter a number: "))
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("The sum of all even numbers from 1 to", n, "is:", sum)