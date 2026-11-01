##Print all numbers from 1 to n whose binary representation contains an even number of 1s
n = int(input("Enter n: "))

for i in range(1, n + 1):
    binary = bin(i)[2:]
    count = binary.count('1')

    if count % 2 == 0:
        print(i)
