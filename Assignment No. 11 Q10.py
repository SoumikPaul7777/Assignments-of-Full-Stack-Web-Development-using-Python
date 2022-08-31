n=int(input("Enter the number : "))
rev=0
while(n):
    rev=rev*10+(n%8)
    n>>=3
print(f"Octal equivalent will be : {rev}.")