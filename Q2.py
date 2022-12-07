optimal_solutions=[]

for x in range(min(400//8,120//2)+1):
    y1=(400-8*x)//2
    y2=120-2*x
    
    if y1==y2 or min(y1,y2)==0 or x==0:
        optimal_solutions.append([(x,min(y1,y2)),90*x+25*min(y1,y2)])

else:
    max=0
    for i in optimal_solutions:
        if max<i[1]: max=i[1]
        
    else:
        for i in optimal_solutions:
            if max in i: print("Number of chairs for maximum profit:",i[0][0],"\nNumber of tables for maximum profit:",i[0][1],"\nMaximum Profit: $"+str(i[1]))