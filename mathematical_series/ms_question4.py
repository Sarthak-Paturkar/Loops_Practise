##Print the **first n terms of an arithmetic progression** for the given first term and common difference.
n = int(input("Enter total number of terms: "))
a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
for i in range(1,n+1):
    print(a,end = " ")
    b = a + d
    a = b
