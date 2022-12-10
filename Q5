def f(x):                                                                       #Defining factorial
    prod=1
    for i in range(1,x+1):
        prod*=i
    
    return prod    

def sin(x):                                                                     #Defining sin function as expansion
    sum=0
    
    for i in range(75):
        sum=sum+((-1)**i)*x**(2*i+1)/f(2*i+1)
        
    return sum

def cos(x):                                                                     #Defining cos function as expansion
    sum=0
    
    for i in range(75):
        sum=sum+((-1)**i)*x**(2*i)/f(2*i)
        
    return sum

def tan(x):                                                                     
    return sin(x)/cos(x)

pi=3.14

angle=float(input("Enter angle in degrees: "))
distance=float(input("Enter distance from pole: "))

print("Height of pole is", round(tan(pi/180*angle)*distance,4),"metres")        #Converting degrees to radians and calculating height 