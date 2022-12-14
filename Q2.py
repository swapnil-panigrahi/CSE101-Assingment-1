optimal_solution=[]                                                                    #list of corner points of the feasible region
M=int(input("Enter value of 'M': "))

for x in range(min(400//8,120//2)+1):                                                  #checking the linear equations for all x in [0, corner point where y=0]
    y1=(400-8*x)//2
    y2=120-2*x                                                                         #solving y for both linear equations
        
    if y1==y2 or min(y1,y2)==0 or x==0:                                                #checking if optimal solutions are acquired for the given value of x and adding it to the list
        
        if x>M and min(y1,y2)>M:
            profit=100*(x-M)+90*M+30*(min(y1,y2)-M)+25*M                               #checking for all cases of M
        
        elif x<=M and min(y1,y2)>M:
            profit=90*x+30*(min(y1,y2)-M)+25*M
        
        elif x>M and min(y1,y2)<=M:
            profit=100*(x-M)+90*M+25*min(y1,y2)
            
        else:
            profit=90*x+25*min(y1,y2)                                   

        optimal_solution.append([(x,min(y1,y2)),profit])                               #solution are added to the list in the format [(x,y),z] where z is the profit

else:                                                                                  #after the for loop is completed, else block is executed
    max=0
    for i in optimal_solution:
        if max<i[1]: max=i[1]                                                          #checking for the maximum profit
        
    else:
        for i in optimal_solution:
            if max in i: print("Number of chairs for maximum profit:",i[0][0],"\nNumber of tables for maximum profit:",i[0][1],"\nMaximum Profit: $"+str(i[1]))