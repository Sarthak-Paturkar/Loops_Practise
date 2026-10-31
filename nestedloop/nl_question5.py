## Print the **Fibonacci pattern row by row**, where each row prints the next Fibonacci numbers
n=int(input("Any number: "))
a=0
b=1
for i in range(1,n+1):
    for j in range(i):
        print(a,end=" ")
        c = a+b
        a = b
        b = c

    print()