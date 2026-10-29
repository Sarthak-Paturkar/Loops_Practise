## Find the HCF (Highest Common Factor) of two given numbers
a = int(input())
b = int(input())
i = 1
hcf = 1
while i<=a and i<=b:
    if a % i == 0 and b % i == 0:
        hcf = i
    i+=1
print("hcf:",hcf)