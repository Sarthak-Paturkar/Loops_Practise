##Find and print the sum of the Fibonacci series.
num = int(input("Enter a number : "))
a = 0
b = 1
sum = 0
for i in range(1,num+1):
    print(a)
    sum+=a
    c = a + b
    a = b
    b = c
print(sum)