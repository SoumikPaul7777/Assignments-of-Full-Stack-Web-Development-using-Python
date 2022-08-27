l=[eval(i) for i in input("Enter the list elements :\n").split()]
ele=eval(input("Enter the any element : "))
print(f"{ele} present not in the list." if ele not in l else f"{ele} present in the list.")