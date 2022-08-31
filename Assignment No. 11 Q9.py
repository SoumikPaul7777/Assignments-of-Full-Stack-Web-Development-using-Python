n=int(input("Enter the number : "))
rev=0
while(n):
    rev=rev*10+(n%2)
    n>>=1
print(f"Binary equvalent is : {rev}.")