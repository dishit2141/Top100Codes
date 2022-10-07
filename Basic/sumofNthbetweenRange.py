#using formula int(n1*(n1+1)/2) - int(n2*(n2+1)/2)

num1 = int(input("Enter staring value to find sum:"))
num2 = int(input("Enter Ending value to find sum:"))
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(f"Sum of {num1} to {num2} is:",sum)