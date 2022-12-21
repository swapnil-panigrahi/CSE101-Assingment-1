cost=int(input("Enter cost: "))
allowance=int(input("Enter monthly allowance: "))
sf=float(input("Saving fraction: "))
r=float(input("Enter rate of interest: "))

savings=2000
months=1

while cost>savings:
    
    savings=(savings*(1+r/100)+allowance*sf)
    months+=1
else:
    savings=(savings*(1+r/100))
    
print(months, "Months")
print(round(savings-cost,3), "will be left as savings!")

def bonus(cost,allowance,r):
    months=int(input("Enter number of months: "))
    sf=(cost/(allowance*((1+r/100)**(months)-1)))*(r/100)
    
    return sf

print("Saving fractions should be:",bonus(cost,allowance,r))