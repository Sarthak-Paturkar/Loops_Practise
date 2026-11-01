##Keep taking numbers from the user and print them until a negative number appears, then stop the loop.
while True:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative number found")
        break

    print(num)