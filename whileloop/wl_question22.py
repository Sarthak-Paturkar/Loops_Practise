## Print the cube of each number from 1 to n.
n = int(input("Print any number : "))
i = 1
count = 0
while count<n:
    digit = i ** 3
    count+=1
    i+=1
    print(digit)