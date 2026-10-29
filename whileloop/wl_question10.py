##Find and print the product of all digits of a given number
n = int(input("Enter a number: "))
product = 1
while n!=0:
    last_digit = abs(n) % 10
    product = product * last_digit
    n = abs(n)//10
print(product)
