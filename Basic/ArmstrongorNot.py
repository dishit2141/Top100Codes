num = 371
temp,sum = num,0
length = len(str(num))
for i in range(length):
    digit = int(temp % 10)
    temp = temp/10
    sum += pow(digit, length)
if sum == num:
    print(f"{num} is Armstrong")
else:
    print(f"{num} is not Armstrong")
