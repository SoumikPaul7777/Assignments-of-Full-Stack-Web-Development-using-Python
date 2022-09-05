tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
print(tuple(sorted(tuple1,key=lambda t1:t1[-1])))