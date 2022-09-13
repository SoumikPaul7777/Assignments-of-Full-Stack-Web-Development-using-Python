def printFirstNNaturalNumbersInReverseOrder(n):
    if n>0:
        print(n,end=" ")
        printFirstNNaturalNumbersInReverseOrder(n-1)
printFirstNNaturalNumbersInReverseOrder(int(input("Enter the number : ")))