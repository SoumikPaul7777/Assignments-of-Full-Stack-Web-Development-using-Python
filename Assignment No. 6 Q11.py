monthNo=int(input("Enter the month number : "))
print("It has","31 days" if monthNo in [1,3,5,7,8,10,12] else "30 days" if monthNo in [4,6,9,11] else "28 or 29 days.")