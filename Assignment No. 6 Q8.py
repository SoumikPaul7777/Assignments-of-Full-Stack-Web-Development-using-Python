a,b,c=[int(input(f"Enter the value of {chr(i)} : ")) for i in range(97,100)]
d=b*b-4*a*c
print("It has real and distinct roots." if d>0 else "It has real and equal roots." if d==0 else "It has imaginary roots.")