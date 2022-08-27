l=[eval(i) for i in input("Enter the list elements :\n").split()]
ele=eval(input("Enter the any element : "))
print(f"{ele} present in the list." if ele in l else f"{ele} present not in the list.")