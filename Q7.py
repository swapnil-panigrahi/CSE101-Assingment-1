cost=int(input("Enter cost: "))
allowance=int(input("Enter monthly allowance: "))
sf=float(input("Saving fraction: "))
r=float(input("Enter rate of interest: "))

savings=allowance*sf
months=1

while cost>savings:
    
    savings=(savings*(1+r/100)+allowance*sf)
    months+=1
else:
    savings=(savings*(1+r/100))
    
print(months, "Months")
print(round(savings-cost,3), "will be left as savings!")

savings=allowance*sf

def bonus(cost,allowance,r):
    months=int(input("Enter number of months: "))
    sf=(cost/(allowance*((1+r/100)**(months-1)-1)))*(r/100)
    
    return sf

saving_frac=bonus(cost,allowance,r)

if saving_frac>1:
    print("Not possible")
else:
    print("Saving fractions should be:",saving_frac)