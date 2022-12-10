import math

def f(t):
    return 2000*math.log(140000/(140000-2100*t))-9.8*t                      #Defining function of velocity as given

a=int(input("Enter start time: "))
b=int(input("Enter end time: "))

distance=0

while a<b:
    distance=distance+0.25*(f(a)+f(a+0.25))/2                               #Calculating distance travelled in t to t + delta t time
    a+=0.25

print("Distance travelled:",round(distance,3),"metres")