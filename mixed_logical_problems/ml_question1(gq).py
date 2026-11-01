##Print all numbers between 1 and 100 whose sum of digits is even
for i in range(1,101):
    temp = i
    sum = 0
    while temp>0:
        digit = temp % 10
        sum+=digit
        temp=temp//10
    if sum % 2 == 0:
        print(i)
    else:
        pass
