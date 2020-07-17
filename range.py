lst = []
n = int(input("enter num of elements: "))
for i in range(0,n):
    ele = int(input("enter elements: "))
    lst.append(ele)
print("input list1=" ,lst)
lst1=[]
for j in lst:
    if j>0:
        lst1.append(j)
print("output list2=" ,lst1)
    

