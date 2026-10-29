##Calculate and print the factorial of a given number
n = int(input("Enter any given number: "))
i = 1
while i<=n:
    factorial = n * i
    i+=1
print("The factorial of ",n,"is",factorial)