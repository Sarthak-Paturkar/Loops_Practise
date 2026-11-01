##Calculate and print the value of the series:

##x − x²/2! + x³/3! − x⁴/4! + ...

'''n = int(input("Enter any number (n): "))
x = int(input("Enter x: "))

total = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i

    if i % 2 != 0:
        term = (x ** i) / fact
    else:
        term = -(x ** i) / fact

    print(term, end="")

    

    total += term

print()
print("Sum:", total)'''


n = int(input("Enter any number (n): "))
x = int(input("Enter x: "))

total = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i

    term =  ((-x) ** i) / -(fact)
    

    total += term

print()
print("Sum:", total)