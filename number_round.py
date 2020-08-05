import random
import numpy as np


# Number game,
# will need a target value - done
# numbers - done
# small numbers - done
# big numbers - done
# number store - done
# A target generator - done
# solutions finder 
# - 

class NumberRound:
	# The class for the number rounds
	def __init__(self):
		self.numbers = []
		self.target = 0
		self.small_numbers = np.repeat(np.linspace(1,10, 10, dtype=int), 2)
		self.big_numbers = np.linspace(25, 100, 4, dtype=int)

	def change_target(self):
		self.target = random.randint(0,999)

	def return_target(self):
		return self.target

	def add_number(self, big=False):
		# Is the number big or small
		if big == True:
			size = self.big_numbers
		else:
			size = self.small_numbers
		# Find array length
		n = len(size)
		# Generate an index based on array length
		x = size[random.randint(0,n-1)]
		# Index of target element
		idx = np.where(size == x)[0][0]
		# Find and remove target element
		if big == True:
			self.big_numbers = np.delete(self.big_numbers, idx)
		else:
			self.small_numbers = np.delete(self.small_numbers, idx)
		# store the number
		self.numbers.append(x)
		#return x

# Numbers game 5 numbers 1 big 
# new_game = NumberRound()
# new_game.change_target()

# new_game.add_number(False)
# new_game.add_number(False)
# new_game.add_number(False)
# new_game.add_number(False)
# new_game.add_number(False)
# new_game.add_number(True)
# print(new_game.numbers)
# print(new_game.target)

class NumberSolver:
	""" This Class is used to solve the number rounds it works by
		taking the input values and converts them into equations 
		using mathematical operators +, -, *, / """
	def __init__(self, numbers, target):
		# Define the operators
		self.add = lambda a,b: a+b
		self.sub = lambda a,b: a-b
		self.mul = lambda a,b: a*b
		self.div = lambda a,b: a/b if a % b == 0 else 0/0
		# Create a list of operators
		self.operators = [(self.add, '+'), (self.sub, '-'), (self.mul, '*'), (self.div, '/')]
		self.numbers = numbers
		self.target = target
		#lists
		self.equation, self.solutions = [], []

# 	def equation_solver(equation):
# 	# Function to solve the value of the equation
# 		for i in range(len(equation)):
# 			# Store the first value as the current result
# 			if i == 0:
# 				result = equation[i]

# 			# Handle new parts of the equation
# 			else:
# 				# All odd values of i will be operators and even ints
# 				if i % 2 != 0:
# 					result = equation[i][0](result, equation[i+1])

# 		return result

	# def Solve(self):

	# 	def equation_solver(equation):
	# 	# Function to solve the value of the equation
	# 		for i in range(len(equation)):
	# 			# Store the first value as the current result
	# 			if i == 0:
	# 				result = equation[i]

	# 			# Handle new parts of the equation
	# 			else:
	# 				# All odd values of i will be operators and even ints
	# 				if i % 2 != 0:
	# 					result = equation[i][0](result, equation[i+1])

	# 	def looper(self):

	# 	    for n in range(len(self.numbers)):
	# 	        self.equation.append( self.numbers[n] )

	# 	        remaining = self.numbers[:n] + self.numbers[n+1:]

	# 	        if equation_solver(self.equation) == self.target:
	# 	        	self.equation_str = ''
	# 	        	for i in self.equation:
	# 	        		if type(i) == int:
	# 	        			equation_str += str(i)
	# 	        		else:
	# 	        			equation_str += i[1]
	# 	        	self.solutions.append(self.equation_str)

	# 	        if len(remaining) > 0:
	# 	            for op in self.operators:
	# 	                self.equation.append(op)
	# 	                self.equation, self.solutions = self.Solve()
	# 	                self.equation = self.equation[:-1]

	# 	        self.equation = self.equation[:-1]

	# 	    return self.equation, self.solutions

	# 	looper(self)

	# 	return self.solutions


#NumberSolver([5,4,3], 23).Solve()
# n = NumberSolver([5,6,7,8], 14)
# print(n.Solve())


add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b if a % b == 0 else 0/0
# Create a list of operators
operators = [(add, ' + '), (sub, ' - ')]#, (mul, ' * '), (div, ' / ')]

#rint(solve_test([], [5,6]))
# Need an eval function for this

def equation_solver(equation):
	# Function to solve the value of the equation
	for i in range(len(equation)):
		# Store the first value as the current result
		if i == 0:
			result = equation[i]

		# Handle new parts of the equation
		else:
			# All odd values of i will be operators and even ints
			if i % 2 != 0:
				result = equation[i][0](result, equation[i+1])

	return result



def Solve(equation, nums, target, solutions):

	def equation_solver(equation):
	# Function to solve the value of the equation
		for i in range(len(equation)):
			# Store the first value as the current result
			if i == 0:
				result = equation[i]

			# Handle new parts of the equation
			else:
				# All odd values of i will be operators and even ints
				if i % 2 != 0:
					result = equation[i][0](result, equation[i+1])

		return result

	def recursion(equation, nums, target, solutions):
	    for n in range(len(nums)):
	        equation.append( nums[n] )

	        remaining = nums[:n] + nums[n+1:]

	        if equation_solver(equation) == target:
	        	equation_str = ''
	        	for i in equation:
	        		if type(i) == int:
	        			equation_str += str(i)
	        		else:
	        			equation_str += i[1]
	        	solutions.append(equation_str)

	        if len(remaining) > 0:
	            for op in operators:
	                equation.append(op)
	                equation, solutions = recursion(equation, remaining, target, solutions)
	                equation = equation[:-1]

	        equation = equation[:-1]

	    return equation, solutions

	equation, ans = recursion(equation, nums, target, solutions)

	return ans

s = Solve([], [5,6,7,8], 14, [])
print(min(s, key=len))

