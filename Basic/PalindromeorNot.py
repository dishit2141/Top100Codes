#using simple iteration
num = int(input("Enter any number to check whether it is palindrome or not:"))
reverse = 0
temp=num
while temp>0:
    remainder = temp % 10
    reverse = (reverse*10) + remainder
    temp = temp // 10
if num == reverse:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")

#using string slicing
num = input("Enter any number to check whether it is palindrome or not:")
reverse = str(num)[::-1]
print(f"{num} is palindrome" if num==reverse else f"{num} is not palindrome")