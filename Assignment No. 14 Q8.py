l=[eval(i) for i in input("Enter the elements separated by space are : ").split()]
temp=[]
for i in l:
    if i not in temp:
        print(f"{i} ----> {l.count(i)}")
        temp.append(i)