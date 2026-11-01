##Print Stars in Even Numbers (2, 4, 6, 8, 10)
n = int(input("Enter the number of stars to print: "))
for i in range(2, n + 1, 2):
    for j in range(i):
        print("*", end="")
    print()