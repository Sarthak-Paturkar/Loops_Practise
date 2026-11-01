#Print the Following Alphabet Pattern
'''
A
B B
C C C
D D D D
E E E E E
'''
for i in range(1, 6):
    for j in range(i):
        print(chr(64 + i), end=" ")
    print()