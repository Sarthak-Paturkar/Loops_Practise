##Find and print the **sum of all factors** of the given number.
#Print all factors of the given number.
num = int(input("Enter a number : "))
sum=0
for i in range(1,num+1):
    if num % i == 0:
        print(i,end=" ")
        sum+=i
print()
print(sum)