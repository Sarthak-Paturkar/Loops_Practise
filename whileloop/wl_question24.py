## Print all factors of the given number
n = int(input("Any number:"))
i = 1
while i<=n:
    if n % i == 0:
        print(i)

    i+=1