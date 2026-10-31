##Print all **Pythagorean triplets** whose values are less than or equal to n

n = int(input("Enter the value of n: "))

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            if a * a + b * b == c * c:
                print(a, b, c)
