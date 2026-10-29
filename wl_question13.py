##Check whether the given number is a palindrome
n = int(input("Enter a number: "))
original = n
reverse = 0
while n!=0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)
if original == reverse:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")

