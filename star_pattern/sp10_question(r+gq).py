##Print Stars and Spaces Alternating (Stars and Blank Spaces; b = blank space)
n=int(input("ENter the number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        if j%2==0:
            print("b",end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
    print()