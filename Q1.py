#1.	Write a Python Program to Find LCM?
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
m1=[]
for i in range(2,n1):
    t1=n1
    while t1==1:
        if t1%i==0:
            t1=t1//i
        m1.append(t1)
print(m1)

