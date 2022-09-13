def printFirstNNaturalNumbers(n):
    if n>0:
        printFirstNNaturalNumbers(n-1)
        print(n,end=" ")
printFirstNNaturalNumbers(int(input("Enter the number : ")))