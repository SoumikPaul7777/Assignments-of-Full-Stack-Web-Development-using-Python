comp=complex(input("Enter the number : "))
print(f"{comp.real}-----> real part is greater." if comp.real>comp.imag else f"{comp.imag}-----> imaginary part is greater.")