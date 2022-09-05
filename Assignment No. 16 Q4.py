t1,t2=[tuple([eval(i) for i in input(f"Enter the {i+1}st/nd number in tuple separated by comma : ").split()]) for i in range(2)]
print(f"Before Swapping :\nt1={t1}\nt2={t2}")
t1,t2=t2,t1
print(f"After Swapping :\nt1={t1}\nt2={t2}")