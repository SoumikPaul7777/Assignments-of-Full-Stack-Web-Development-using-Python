num1,num2=[int(input(f"Enter the number {i+1} is : ")) for i in range(2)]
print(f"Before Swapping :\nnum1={num1}\nnum2={num2}")
num1,num2=num2,num1
print(f"After Swapping :\nnum1={num1}\nnum2={num2}")