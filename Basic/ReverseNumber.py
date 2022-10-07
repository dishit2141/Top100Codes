#using simple iteration
num = int(input("Enter number to reverse:"))
temp=num
reverse=0
while num>0:
    remainder = num%10
    reverse = (reverse*10)+remainder
    num = num//10
print(reverse)

# using String Slicing

num1 = input("Enter number to Reverse:")
print(str(num1)[::-1])