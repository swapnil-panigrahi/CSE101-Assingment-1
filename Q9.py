from math import e

def D(a,b,p):
    return e**(a-b*p)

def S(c,d,p):
    return e**(c+d*p)

a,b,c,d=10,1.05,1,1.06

price=1
while D(a,b,price)>S(c,d,price):
    price*=1.05
else:
    if D(a,b,price)>S(c,d,price)+50:
        print("No solution")
    else:
        print("Equilibrium price when 5% increase in price:",price)
        print("Demand: ", D(a,b,price))
        print("Supply: ", S(c,d,price))