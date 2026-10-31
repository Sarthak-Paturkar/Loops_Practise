##Calculate and print the value of the series:

   ## 1 + 1/2 + 1/3 + ... + 1/n

'''n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n+1):
    print(1/i,"+",end=" ")
    sum+=1/i
print()
print(sum)'''

n = int(input("Enter the value of n: "))
total = 0
for i in range(1, n + 1):
    print(f"1/{i}", end="")
    if i < n:
        print(" + ", end="")
    total += 1/i
print()
print("Sum:", total)
