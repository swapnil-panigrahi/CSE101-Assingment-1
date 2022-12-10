def sum(x):
    sum=0
    for i in x:
        sum+=i
    return sum

pop = [50, 1450, 1400, 1700, 1500, 600, 1200]
grate=[2.5,2.1,1.7,1.3,0.9,0.5,0.1]

y=int(input("Enter the number of years: "))

population_n=0
current_pop=0
max_pop=0
n=0

for i in range(y):
    current_pop=sum(pop)
    n+=1
    
    print("Population in year "+str(n)+":",round(current_pop,3),"million")
    
    for i in range(7):
        pop[i]=pop[i]*(1+grate[i]/100)
            
    for i in range(7):
        grate[i]-=0.1
    
    population_n=sum(pop)
    
    if current_pop<population_n:    
        max_year=n
        max_pop=population_n

else:
    print("Maximum population:",round(max_pop,3),"million","\nPopulation will reach it's maximum after "+str(max_year)+" years")
