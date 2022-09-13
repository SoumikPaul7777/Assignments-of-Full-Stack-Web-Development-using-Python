def printFirstNEvenNaturalNumbersInReverseOrder(n):
    if n>0:
        print(2*n,end=" ")
        printFirstNEvenNaturalNumbersInReverseOrder(n-1)
printFirstNEvenNaturalNumbersInReverseOrder(int(input("Enter the number : ")))