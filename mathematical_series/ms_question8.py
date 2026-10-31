##Print the series of powers of two:

##1 + 2 + 4 + 8 + ... + 2ⁿ
n=int(input("Enter any number: "))
sum=0
for i in range(0, n+1):
    print((f"2 ** {i}"),end =" ")
    if i<n:
        print("+",end=" ")
    sum+=2**i
print()
print(sum)