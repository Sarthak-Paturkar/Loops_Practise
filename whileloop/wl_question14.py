##Find and print the sum of digits of the given number
n =int(input())
sum=0
while n!=0:
    digit = n%10
    sum+=digit
    n=n//10
print(sum)