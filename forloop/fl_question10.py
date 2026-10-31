##Print the Fibonacci series up to the required number of terms
num = int(input("Enter any number: "))
a = 0
b = 1
for i in range(1,num+1):
    print(a)
    c = a + b
    a = b
    b = c
