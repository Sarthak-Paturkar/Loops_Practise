##Print Numbers in an increasing sequence
n=int(input("ENter the required number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()