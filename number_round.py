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

class NumberSolver:
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

	# I need to loop de loop
	# This will be to loop the numbers and the operator combinations
	def Solve(self):
		# loop the numbers
		total = 0
		equation = []
		for i, n in enumerate(self.numbers):
			#print(n)
			equation.append(n)
			print(equation)

			#total = self.add(total, n)
			print(total)


#NumberSolver([5,4,3], 23).Solve()

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


# Solution generator
# 6 numbers
# 4 operators
# Number of possibilities 6*4*6*4*6*4*6*4*6*4*6*4
# 191102976 possible combinations
#print(6*4*6*4*6*4*6*4*6*4*6*4)


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



def Solve(equation, nums, target):

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
        	print(equation_str)

        if len(remaining) > 0:
            for op in operators:
                equation.append(op)
                equation = Solve(equation, remaining, target)
                equation = equation[:-1]

        equation = equation[:-1]

    return equation

Solve([], [5,6,7,8], 14)