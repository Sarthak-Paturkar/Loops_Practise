##Find and print the **sum of the first n natural numbers**
n=int(input("Enter any number (n): "))
natural_num_sum = 0
for i in range(1,n+1):
    natural_num_sum += i
print(natural_num_sum)