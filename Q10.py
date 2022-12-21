def f(x):                                                                                       #Defining function
    return x**3-10.5*x**2+34.5*x-35

def df(x):                                                                                      #Defining derivative
    return 3*x**2-2*10.5*x+34.5

y=float(input("Enter value of x:"))
x=y

def roots(y,x):
    while y<=x:
        x=y-f(y)/df(y)
        if round(y,4)==round(x,4):
            return x
            break
        y=x
        
print(roots(y,x))

def bonus(x1,x2):
    res=[]
    
    for i in range(x1,x2+2):
        if roots(i,x)!=None:
            res.append(round(roots(i,x),3))
        
    return res

x1=int(input("Enter initial value: "))
x2=int(input("Enter final value: "))

for i in set(bonus(x1,x2)):
    print(i,end=" ")