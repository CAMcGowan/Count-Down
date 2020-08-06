import random
import numpy as np

class NumberRound:
	# The class for the number rounds
	def __init__(self):
		self.numbers = []
		self.target = 0
		self.small_numbers = np.repeat(np.linspace(1,10, 10, dtype=int), 2)
		self.big_numbers = np.linspace(25, 100, 4, dtype=int)
		# Define the operators
		self.add = lambda a,b: a+b
		self.sub = lambda a,b: a-b
		self.mul = lambda a,b: a*b
		self.div = lambda a,b: a/b if a % b == 0 else 1e6 #if a decimal this isn't allowed, so the large number will make the target answer impossible
		# Create a list of operators
		self.operators = [(self.add, '+'), (self.sub, '-'), (self.mul, '*'), (self.div, '/')]
		self.nums = []
		self.target = 0
		# lists
		self.equation, self.solutions = [], []

	def change_target(self):
		self.target = random.randint(0,999)

	def return_target(self):
		return self.target

	def add_big(self):
		# Find array length
		n = len(self.big_numbers)
		# Generate an index based on array length
		x = self.big_numbers[random.randint(0,n-1)]
		# Index of target element
		idx = np.where(self.big_numbers == x)[0][0]
		# Find and remove target element
		self.big_numbers = np.delete(self.big_numbers, idx)
		# store the number
		self.nums.append(x)

	def add_small(self):
		# Find array length
		n = len(self.small_numbers)
		# Generate an index based on array length
		x = self.small_numbers[random.randint(0,n-1)]
		# Index of target element
		idx = np.where(self.small_numbers == x)[0][0]
		# Find and remove target element
		self.small_numbers = np.delete(self.small_numbers, idx)
		# store the number
		self.nums.append(x)

	def solve(self):

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
		    	# Add the number to the equation
		        equation.append( nums[n] )

		        # Return the remaining numbers
		        remaining = nums[:n] + nums[n+1:]

		        # Before going futher check if the equation equals the target value
		        if equation_solver(equation) == self.target:
		        	# Create a readable string to output the equation
		        	equation_str = ''
		        	# Check type before storing part of equation
		        	for i in equation:
		        		# checks for any int due to numpy int32
		        		if np.issubdtype(type(i), int) == True:
		        			equation_str += str(i)
		        		else:
		        			equation_str += i[1]
		        	solutions.append(equation_str)

		        # If there are still numbers left and target not reached
		        if len(remaining) > 0:
		            for op in self.operators:
		            	# Add a new operator
		                equation.append(op)
		                # Use recursion to repeat this step for all possible scenarios
		                equation, solutions = recursion(equation, remaining, self.target, solutions)
		                equation = equation[:-1]

		        equation = equation[:-1]

		    return equation, self.solutions

		equation, ans = recursion(self.equation, self.nums, self.target, self.solutions)

		if len(ans) > 0:
			return ans
		else:
			return ['No solutions']

# Numbers game 5 numbers 1 big 
new_game = NumberRound()
new_game.change_target()

new_game.add_small()
new_game.add_small()
new_game.add_small()
new_game.add_small()
new_game.add_small()
new_game.add_big()
print(new_game.nums)
print(new_game.target)
s = new_game.solve()
print(min(s, key=len))