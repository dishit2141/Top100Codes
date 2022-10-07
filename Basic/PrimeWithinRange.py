start = 0
end = int(input("Enter Ending number to find Prime till that:"))
prime=[]
for i in range(2,end+1):
    flag=0
    if i<2:
        continue
    if i==2:
        prime.append(2)
        continue
    for x in range(2,i):
        if i%2==0:
            flag=1
            break
    if flag==0:
        prime.append(i)
print(prime)

