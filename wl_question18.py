##Check whether the given number is a prime number.
n = int(input("Enter a number: "))
if n<2:
    print("Not a Prime Number")
else:
    i=2
    while i<n:
        if n % i == 0:
            break
        i+=1
    if i == n :
        print("Prime Number")
    else:
        print("Not a prime number")
