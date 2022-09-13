def printFirstNMultiplesOfAGivenNumber(n,i):
    if i>0:
        printFirstNMultiplesOfAGivenNumber(n,i-1)
        print(f"{n*i}",end=" ")
printFirstNMultiplesOfAGivenNumber(int(input("Enter a number : ")),int(input("How many multiples of a number : ")))