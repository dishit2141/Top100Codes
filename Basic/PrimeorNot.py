num = int(input("Enter Any Number to check whether it's prime or not:"))
flag=0
if num<2:
    flag=1
else:
    for i in range(2,num+1):
        if num%2==0:
            flag=1
            break
if flag==1:
    print(f"{num} is not Prime")
else:
    print(f"{num} is Prime")