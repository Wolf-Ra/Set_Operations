A=set()
B=set()
n1=int(input("Enter the No of Elements in set A : "))
n2=int(input("Enter the No of Elements in Set B : "))
for i in range(n1):
    print("Enter the ",i+1," Element of A :")
    x=int(input())
    A.add(x)
    i=i+1 
for i in range(n2):
    print("Enter the ",i+1," Element of B : ")
    y=int(input())
    B.add(y)
    i=i+1
print("The Union of A and B is : ",A|B)
print("The Intersection of A and B is : ",A&B)
print("The Difference of A and B is : ",A-B)
print("The Symmetric Difference of A and B is : ",A^B)