num = int(input("Enter Nth value to find Fibo Series:"))
n1,n2=0,1
print("Fibo Series",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
    
