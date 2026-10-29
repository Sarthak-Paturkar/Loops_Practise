##Find and print the sum of all factors of the given number
n=int(input("Enter any number: "))
i = 1
sum = 0
while i<=n:
    if n % i == 0:
        print(i)
        sum += i
    i+=1
print(sum)