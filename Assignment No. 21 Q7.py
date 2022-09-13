def printSquaresOfFirstNNaturalNumbers(n):
    if n>0:
        printSquaresOfFirstNNaturalNumbers(n-1)
        print(n*n,end=" ")
printSquaresOfFirstNNaturalNumbers(int(input("Enter the number : ")))