# CSE101 Assingment-1
 First assignment of IP (python3), let's see how it goes :D 
 
 Feel free to refer to my codes in case you are stuck at any problem (please don't copy, plag lag jayegi 🗿)

 ## 1. Lots of ifs and else
 Write a program to take as input a number between 0 and 99, and print the text equivalent of the number. i.e., for inputs 5, 13, 43, and 85, outputs are `five`, `thirteen`, `forty three`, and `eighty five`. ~~(Hint: Have a function to write the text for tens digit, and another to write the text for the unit digit - use of elif construct will be helpful in these. In main, take the input, get the decimal and units digits of the number and print their text. The code is simple though it may be long as you have to print for different cases. You may first write a function to print the text for a units digit and test it, and then build the rest)~~

> Bonus Question. Expand the code above to write in text any number lesser than 100 crore. (FYI we have: units, tens, hundred, thousand, ten-thousand, lac, ten-lac, crore, ten-crore).

## 2. LPP (Linear Pog Programming)
Two variable optimization. Many problems require optimization of some function – minimizing (e.g., loss) or maximizing (e.g., profit) given some function and some constraints. This is an example of this problem.

A furniture company manufactures dining room tables and chairs. The relevant manufacturing data are given in the table

| Department | Labor-Hours per Tables | Labor-hrs per Chairs | Maximum Labor-Hours | Available/day |
| ---------- | ---------------------- | -------------------- | ----------------------------------- |
| Assembly | 8 | 2 | 400 |
| Finishing | 2 | 1 | 120 |
| Profit per Unit | $90 for first M units, $100 after that | $25 for first M units, $30 after that |


Write a program to determine how many tables and chairs should be manufactured each day to realize a maximum profit. Print the number of chairs, tables, and the maximum profit. Initially have M = 10. Run the program again for M = 0, 20 and see how the output changes. Keep the code to compute this simple (even if it is inefficient), and you do not have to optimize the code.

Hint: Let x1 represent the number of tables and x2 represent the number of chairs. Determine the equations for total profit P, and the constraints on the two types of labor hours. Write functions to compute P and each constraint (these will be very simple functions). Have a statement in main program to set M and pass it to function for computing profit - you can change the value of M for different runs of the program. Write the main program that ranges over the values of x1 and x2 (from min possible value to max possible value) to find at which values max is reached.
