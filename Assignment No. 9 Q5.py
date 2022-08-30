n=int(input("Enter the number : "))
print(f"First {n} odd natural numbers in reverse order are : ")
while(n>=1):
    print(2*n-1,end=" ")
    n-=1