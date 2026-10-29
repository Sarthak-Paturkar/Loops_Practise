n=int(input("Enter a number: "))
i=1
total=0
while i<n:
    if n%i == 0:
        total+=i
    i+=1

if total == n:
    print("It's a Perfect numnber")
else:
    print("It's not a perfect number")