
# Python 100, Session 01, Task 5, Part 1
# this code builds a grid that is made up of "+", "-", and "|" characters 
# n is th number of lines built each time the func is called.

def print_grid(n):

	# makes columnNum columns of one row of the "+ - - - - +" wall
	def horizWall(columnNum):    
		unit = "+ - - - - "
		fullWall = unit*columnNum
		print(fullWall + "+")

	# builds columnNum columns of one row of the "|         |" wall 
	def vertWall(columnNum):
		unit = "|         "
		fullWall = unit*columnNum
		print(fullWall+"|")

	# calls the above two functions to build n rows and n columns of the grid
	for i in range(0,n): #runs the code inside n times to build n rows of the grid
		horizWall(n)
		for i in range(0,4): #uses the vertical wall 4 times for each row
			vertWall(n)
	horizWall(n)    #makes bottom wall to close the grid

   # example: makes a 4 X 4 grid
print_grid(4)


# The code below was my first go at the problem. See above for my imporved solution:
# def plusMinus(n):
# 	for i in range(0,n):
# 		print("+ - - - - + - - - - +")

# def barlines(n):
# 	for i in range(0,n):
# 		print("|         |         |")

# def blockBuilder(n):
# 	for i in range(0,n):
# 		plusMinus(1)
# 		barlines(4)

# # build two blocks and one closing wall (plusMinus is the closing wall)
# blockBuilder(2)
# plusMinus(1)
