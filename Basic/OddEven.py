#Brute force method

input= int(input("Enter any number to check odd or even"))

if input%2==0:
    print(f"{input} is Even")
else:
    print(f"{input} is Odd")

#Ternary method
print(f"{input} is Even" if input%2==0 else f"{input} is Odd")