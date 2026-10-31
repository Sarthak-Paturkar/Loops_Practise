##Find and print the **sum of all even numbers** from 1 up to n
num=int(input("Enter a number: "))
sum_even=0
for i in range(2,num+1,2):
    print(i)
    sum_even += i

print("The total sum is ",sum_even)