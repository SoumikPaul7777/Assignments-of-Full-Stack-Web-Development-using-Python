num1,num2,num3=[int(input(f"Enter the {i+1}st/nd/rd word : ")) for i in range(3)]
if num1!=num2 or num2!=num3 or num3!=num1:
    print(f"Greater number will be : {max(num1,num2,num3)}.")
else:
    print(f"All the three numbers are same.\nNumber is : {num1}")