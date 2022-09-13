rev=0
def printNumberInReverseOrder(num):
    global rev
    if num>0:
        rev=rev*10+num%10
        printNumberInReverseOrder(num//10)
    return rev
print("Reverse is :",printNumberInReverseOrder(int(input("Enter the number : "))))