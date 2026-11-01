#Print all palindrome numbers between 1 and 500.
for i in range(1,501):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp = temp//10
    if rev==i:
        print(i)