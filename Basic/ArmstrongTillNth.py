start = int(input("Enter starting value:"))
end = int(input("Enter Ending value:"))
for n in range(start, end + 1):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=",")
