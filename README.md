# CSE101 Assingment-1
 First assignment of IP (python3), let's see how it goes :D 
 
 Feel free to refer to my codes in case you are stuck at any problem (please don't copy, plag lag jayegi 🗿)

 ## 1. Lots of ifs and else
 Write a program to take as input a number between 0 and 99, and print the text equivalent of the number. i.e., for inputs 5, 13, 43, and 85, outputs are `five`, `thirteen`, `forty three`, and `eighty five`. ~~(Hint: Have a function to write the text for tens digit, and another to write the text for the unit digit - use of elif construct will be helpful in these. In main, take the input, get the decimal and units digits of the number and print their text. The code is simple though it may be long as you have to print for different cases. You may first write a function to print the text for a units digit and test it, and then build the rest)~~

> Bonus Question. Expand the code above to write in text any number lesser than 100 crore. (FYI we have: units, tens, hundred, thousand, ten-thousand, lac, ten-lac, crore, ten-crore).

## 2. LPP (Linear Pog Programming)
Two variable optimization. Many problems require optimization of some function – minimizing (e.g., loss) or maximizing (e.g., profit) given some function and some constraints. This is an example of this problem.

A furniture company manufactures dining room tables and chairs. The relevant manufacturing data are given in the table

| Department      | Labor-Hours per Tables                 | Labor-hrs per Chairs                  | Maximum Labor-Hours Available/day |
| ----------      | ----------------------                 | --------------------                  | --------------------------------- |
| Assembly        | 8                                      | 2                                     | 400                               |
| Finishing       | 2                                      | 1                                     | 120                               |
| Profit per Unit | $90 for first M units, $100 after that | $25 for first M units, $30 after that |                                   |


Write a program to determine how many tables and chairs should be manufactured each day to realize a maximum profit. Print the number of chairs, tables, and the maximum profit. Initially have M = 10. Run the program again for M = 0, 20 and see how the output changes. Keep the code to compute this simple (even if it is inefficient), and you do not have to optimize the code.

~~Hint: Let x1 represent the number of tables and x2 represent the number of chairs. Determine the equations for total profit P, and the constraints on the two types of labor hours. Write functions to compute P and each constraint (these will be very simple functions). Have a statement in main program to set M and pass it to function for computing profit - you can change the value of M for different runs of the program. Write the main program that ranges over the values of x1 and x2 (from min possible value to max possible value) to find at which values max is reached.~~

## 3. Distance vs Displacement
Distance traveled. A vehicle is to travel on demand. Its initial location is given as x0, y0 (assume the first statement in your program as assigning initial values, say x0,y0 = 5.0, 5.0). Repeatedly take as input the distance the vehicle has to travel. If the input given is 0 or lesser, the travel ends - assume that at least one positive distance will be given. The direction in which the vehicle is to travel is determined as follows: if distance is <= 25 it travels north, if between 26-50 it travels south, between 51 and 75 it travels east, and >= 76 it travels west. Find the final coordinate of the vehicle, the total distance it has traveled, and the straight line distance between the initial location and the final location (use standard formula for distance between two coordinates; note that this distance is not same as total distance traveled).

~~Hint: Initialize current coordinates x,y to x0,y0, and distance traveled to 0. For taking the distance use a while loop (as you dont know how many distances will be given). This can be done in two ways - you can initialize a variable (say dist) to some +ve value, and then loop till the value is 0 (or lesser) and in the loop get the input from the user for next distance. Alternatively, you can have an infinite while loop, and take input in the loop and break if the input given is 0 (or lesser). For each input distance, determine the new coordinates, and keep track of total distance traveled. After the loop is done, compute the distance also.~~

## 4. Scuffed Integration
Integration through computation. Suppose the velocity of a rocket at a time t is given by: 
$$f(t) = 2000 \ln(\frac{140000}{140000 - 2100\*t}) - 9.8*t$$
Take as input starting time (a) and ending time (b), and find the distance covered by a rocket between time a and b. For computationally determining the distance, work with time increments (delta) of 0.25 seconds. You can use the math module of python for this problem.

~~Hint: Compute the velocity at time t and t+delta, take the average, and then compute the distance traveled in this delta time duration. Start from a and keep computing in increments of delta till b.~~

## 5. Heights and Distances 
A person is standing and is looking at a pole in front of him. Given the angle of view to the top (in degrees – should be between 0 and 90) and the horizontal distance from the person to the base of the pole (in meters), you have to find the height of the pole and the length of the line from the person to the top of the pole.
 
Your program has to take as input (from the user on the terminal) the angle (in degrees) and another input for distance to the base of the pole. Then it computes and prints the height of the pole and the distance to the tip of the pole.
 
Note. For this question, you must write functions to compute sin(), cos(), … using the series for them and cannot use the python provided functions (e.g., in the math module). If the value of pi is needed, you can use the standard value (3.14). First, write these functions and test them. Then write the main program to take inputs for angle and distance, and call the functions to compute the height and distance.

## 6. 