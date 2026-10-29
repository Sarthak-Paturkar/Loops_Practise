##Calculate and print the sum of the first n natural numbers
n = int(input("Enter any natural number: "))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("The sum of first",n,"natural numbers is:",sum)