##Search for a specific number in a list of inputs, and terminate the loop immediately when the number is found.
numbers = [10, 20, 30, 40, 50]

target = int(input("Enter the number to search: "))

for num in numbers:
    if num == target:
        print("Number found!")
        break
    print(num)