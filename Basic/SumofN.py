#using String Character Extraction
sum=0
num = input("Enter Number")
for i in num:
    sum = sum + int(i)
print(sum)

#using Brute Force
sum=0
num = int(input("Enter Number"))
while num!=0:
    digit = num%10
    sum += digit
    num = num//10
print(sum)