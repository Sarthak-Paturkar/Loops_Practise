#Print the Following Number Pattern
'''
1
2 3
4 5 6
7 8 9 0
1 2 3 4 5
6 7 8 9 0 1
2 3 4 5 6 7 8
'''
n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        if num > 9:
            num = 0
        else:
            num = num
        print(num, end=" ")
        num += 1
    print()