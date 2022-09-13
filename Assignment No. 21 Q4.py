def printFirstNOddNaturalNumbersInReverseOrder(n):
    if n>0:
        print(2*n-1,end=" ")
        printFirstNOddNaturalNumbersInReverseOrder(n-1)
printFirstNOddNaturalNumbersInReverseOrder(int(input("Enter the number : ")))