def printCubesOfFirstNNaturalNumbers(n):
    if n>0:
        printCubesOfFirstNNaturalNumbers(n-1)
        print(n**3,end=" ")
printCubesOfFirstNNaturalNumbers(int(input("Enter the number : ")))