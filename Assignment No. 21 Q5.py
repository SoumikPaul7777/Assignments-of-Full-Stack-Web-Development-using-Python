def printFirstNEvenNaturalNumbers(n):
    if n>0:
        printFirstNEvenNaturalNumbers(n-1)
        print(2*n,end=" ")
printFirstNEvenNaturalNumbers(int(input("Enter the number : ")))