##Find the **HCF (Highest Common Factor)** of the given numbers.
num1 = int(input("Enter any number(1) : "))
num2 = int(input("Enter any number(2) : "))
for i in range(1, min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print("HCF =", i)