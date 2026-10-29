##Print the Fibonacci series up to n terms
n = int(input("Enter any number: "))
a = 0
b = 1
count = 0
while count < n:
    print(a)
    c = a+b
    a = b
    b = c
    count+=1
