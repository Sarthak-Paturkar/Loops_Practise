##Find and print the **sum of all odd numbers** from 1 up to n.
num=int(input("Enter a number: "))
sum_odd=0
for i in range(1,num+1,2):
    print(i)
    sum_odd += i

print("The total sum is ",sum_odd)