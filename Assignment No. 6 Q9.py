year=int(input("Enter the year : "))
print("It is a leap year." if (year%400==0)or(year%4==0 and year%100!=0) else "It is not a leap year.")