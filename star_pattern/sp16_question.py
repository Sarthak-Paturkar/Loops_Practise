##Print the Following Alphabet Pattern
'''
A
B C
D E F
G H I J
K L M N O
'''

char = ord('A')

for i in range(1, 6):
    for j in range(i):
        print(chr(char), end=" ")
        char += 1
    print()