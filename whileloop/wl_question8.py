##Calculate the sum of all odd numbers from 1 up to n
n = int(input("Enter any number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 2
print("The sum of all odd numbers from 1 to n is ",sum)