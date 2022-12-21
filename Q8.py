def sum(x):                                                                     #defining sum since we aren't allowed to use in-built list functions 
    sum=0
    for i in x:
        sum+=i
    return sum

def grate(x,y):                                                                 #Growth Rate function
    return 2.5-0.4*x-0.1*y

pop = [50, 1450, 1400, 1700, 1500, 600, 1200]                                   #population of all 7 groups

population_n=0                                                                  #population of next year initiating as 0
current_pop=0
max_pop=0                                                                       #variable to store maximum population once achieved
n=0

year=int(input("Enter nth year: "))

while n<year:
    for i in range(7):
        pop[i]=pop[i]*(1+grate(i,n)/100)

    n+=1
else:
    print("Nth Year Population:",round(sum(pop),3),"million")

pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

n=0
while current_pop<=population_n:
    current_pop=sum(pop)
    for i in range(7):
        pop[i]=pop[i]*(1+grate(i,n)/100)

    n+=1
    population_n=sum(pop)
    
    if current_pop<population_n:    
        max_year=n
        max_pop=population_n

else:
    print("Maximum population:",round(max_pop,3),"million","\nPopulation will reach it's maximum after "+str(max_year)+" years")    