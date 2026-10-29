```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

i = 1

while True:
    if i % a == 0 and i % b == 0:
        print("LCM:", i)
        break
    i += 1
```