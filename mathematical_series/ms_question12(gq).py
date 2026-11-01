##Check whether the given number is a **Strong number**, where the number equals the sum of the factorials of its digits.
n= int(input("Enter a number: "))
temp=n
sum=0
while temp>0:
    digit =temp%10
    fact = 1
    for i in range(1,digit+1):
        fact=fact*i
    sum+=fact
    temp//=10
if sum==n:
    print(n,"is a Strong number")
else:
    print(n,"is not a Strong number")
    