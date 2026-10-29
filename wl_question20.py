##Find and print the sum of the Fibonacci series up to n terms
n=int(input("Enter any term: "))
a = 0
b = 1
count = 0
sum = 0
while count < n :
    print(a)
    sum += a
    c = a+b
    a = b
    b = c
    count+=1
print(sum)

