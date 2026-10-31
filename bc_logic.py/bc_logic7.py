##Continuously add numbers in a loop and stop the loop when the sum becomes **greater than 100**
i = 0
total = 0
while True:
    total+=i
    if total > 100:
        break
    print(i)
    i+=1
print(total)
