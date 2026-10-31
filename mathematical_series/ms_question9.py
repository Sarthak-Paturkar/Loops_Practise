##Calculate and print the value of the series:

## 1! + 2! + 3! + ... + n!
n = int(input("Enter the value of n: "))
sum = 0
fact = 1
for i in range(1,n+1):
    fact = fact * i
    print(f"{i}!",end=" ")
    sum+=fact
    if i<n:
        print("+",end=" ")
print()
print(sum)
    
