a,b,c=[eval(input(f"Enter the value of side {i+1} is : ")) for i in range(3)]
s=(a+b+c)/2
print(f"Area of a triangle is : {(s*(s-a)*(s-b)*(s-c))**0.5}")