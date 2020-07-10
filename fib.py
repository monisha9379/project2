n=int(input("enter the number of elements:"))
n1=0
n2=1
i=1
n3=0
while i<=n:
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
    i+=1

