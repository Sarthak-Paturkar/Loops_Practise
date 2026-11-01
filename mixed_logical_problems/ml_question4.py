##Print all numbers from 1 to 100 whose sum of digits is a multiple of 3
for i in range(1,101):
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp//10
    if sum%3==0:
        print(i)