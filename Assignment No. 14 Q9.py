l=[int(i) for i in input("Enter the elements :\n").split()]
element=eval(input("Enter the number : "))
start=0
for i in range(l.count(element)):
    print(f"{element} at {l.index(element,start)}")
    start=l.index(element,start)+1