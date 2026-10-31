##Print all **prime numbers** up to n using nested loop checking
num = int(input("Enter a number: "))
is_Prime = True
if num<2:
    is_Prime = False
for i in range(2,num):
    if num % i == 0:
        is_Prime = False
        break

if is_Prime :
    print("Prime number")

else:
    print("Not a prime number")

