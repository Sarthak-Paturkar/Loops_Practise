## Find the **LCM (Least Common Multiple)** of the given numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(max(num1, num2), num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        print("LCM =", i)
        break

'''
max(num1, num2) → Starts from the larger number.
num1 * num2 → Provides an upper limit because the LCM cannot exceed the product of two positive integers.
break → Stops the loop when the first common multiple is found.
'''