## Print a pattern where the i-th row prints the value i × i.
n=int(input("Enter any number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * i,end=" ")
    print()