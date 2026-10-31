##Calculate and print the value of the series:

## 1² + 2² + 3² + ... + n²

n = int(input("Enter total number of numbers: "))
sum = 0
for i in range(1,n+1):
    print(i ** 2,end = " ")
    sum += i ** 2
print()
print(sum)
