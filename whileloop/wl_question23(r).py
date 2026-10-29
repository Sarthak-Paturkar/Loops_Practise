##Print all numbers between a and b that are divisible by 7
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
while a<=b:
    if a % 7 == 0:
        print(a)
    a+=1