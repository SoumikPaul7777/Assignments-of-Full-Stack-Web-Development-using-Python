num=int(input("Enter the number : "))
count=0
while(num):
    count=count+1
    num//=10
print("It is a three digit number." if count==3 else "It is not a three digit number.")