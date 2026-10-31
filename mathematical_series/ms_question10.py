##Calculate and print the value of the series:

##1 + x + x² + x³ + ... + xⁿ
n = int(input("Enter the n: "))
x = int(input("Any real number: "))
sum = 0
for i in range(0,n+1):
    square = x ** i
    print(f"{x} ** {i}",end=" ")
    if i < n:
        print("+",end=" ")
    sum += square
print()
print(sum)