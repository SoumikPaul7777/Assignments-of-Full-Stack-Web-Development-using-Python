def printFirstNOddNaturalNumbers(n):
    if n>0:
        printFirstNOddNaturalNumbers(n-1)
        print(2*n-1,end=" ")
printFirstNOddNaturalNumbers(int(input("Enter the number : ")))