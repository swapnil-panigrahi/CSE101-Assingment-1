x0,y0=map(int,input("Enter coordinates: ").split())                         #Initial Coordinates
distance=float(input("Distance to travel: "))

x=x0                                                                        #Variables which will act as final coordinates
y=y0
distance_travelled=0

while not distance<0:                                                       #Checking if distance is non-negative
    
    if distance<=25:                                                        #Distance conditions as given
        y+=distance
    elif distance<=50:
        y-=distance
    elif distance<=75:
        x+=distance
    else:
        x-=distance
        
    distance_travelled+=distance    
    distance=float(input("Distance to travel: "))

displacement=((x-x0)**2+(y-y0)**2)**0.5                                     #Calculating displacement using distance formula

print("Final coordinates: ("+str(x)+","+str(y)+",")
print("Distance travelled:",distance_travelled)
print("Straight line distance:",displacement)