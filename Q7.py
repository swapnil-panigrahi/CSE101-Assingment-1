cost=int(input("Enter cost: "))
allowance=int(input("Enter monthly allowance: "))
sf=float(input("Saving fraction: "))
r=float(input("Enter rate of interest: "))

savings=0
months=0

while cost>savings:
    savings=(savings*(1+r/100)+allowance*sf)
    months+=1

print(months, "Months")
print(round(savings-cost,3), "will be left as savings!")