#using ternary and brute force

num1 = int(input("Enter 1st value:"))
num2 = int(input("Enter 2nd Value:"))
num3 = int(input("Enter 3rd value:"))
#finding max from two value
print(f"{num1} is greater than {num2}" if num1>num2 else f"{num2} is greater than {num1}")
#finding max from three value
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num1} and {num2} ")
