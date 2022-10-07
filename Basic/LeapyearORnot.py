year = int(input("Enter year from 0001 to 9999 to find it's leap or not"))
print(f"{year} is Leap year" if year%4==0 and year%100!=0 or year%400==0 else f"{year} is not a Leap year")