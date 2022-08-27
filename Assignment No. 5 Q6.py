num=int(input('Enter a three number : '))
print(f"The middle digit will be : {(num-((num//100)*100+num%10))//10}")