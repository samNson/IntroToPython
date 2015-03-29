
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

