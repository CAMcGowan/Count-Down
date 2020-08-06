import random
import numpy as np

class WordRound:
	# A number round
	def __init__(self):
		# Create the letter lists on weights
		self.consonants_weights = [ ('B',2), ('C',3), ('D',6), ('F',2), ('G', 3), ('H',2),
									('J',1), ('K',1), ('L',5), ('M',4), ('N',8), 
									('P',4), ('Q',1), ('R',9), ('S',9), ('T',9),  
									('V',1), ('W',1), ('X',1), ('Y',1), ('Z',1)]
		self.vowels_weights = [ ('A',15), ('E',21), ('I',13), ('O',13), ('U',5)]
		# Loop to create a weighted list of Consonants
		self.consonants_list = []
		for item, weight in self.consonants_weights:
		    self.consonants_list.extend( [item]*weight )
		self.consonants_list = np.array(self.consonants_list)	
		# Loop to create a weighted list of vowels
		self.vowels_list = []
		for item, weight in self.vowels_weights:
		    self.vowels_list.extend( [item]*weight )
		self.vowels_list = np.array(self.vowels_list)
		# List to store letters
		self.letters = []

	def add_consonant(self):
		# Selecting a letter
		letter = random.choice(self.consonants_list)
		# Index of target element
		idx = np.where(self.consonants_list == letter)[0][0]
		# Remove letter from list
		self.consonants_list = np.delete(self.consonants_list, idx)
		# Store the letter
		self.letters.append(letter)

	def add_vowel(self):
		# Selecting a letter
		letter = random.choice(self.vowels_list)
		# Index of target element
		idx = np.where(self.vowels_list == letter)[0][0]
		# Remove letter from list
		self.vowels_list = np.delete(self.vowels_list, idx)
		# Store the letter
		self.letters.append(letter)

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


# run a word round
word = WordRound()
word.add_vowel()
word.add_vowel()
word.add_vowel()
word.add_consonant()
word.add_consonant()
word.add_consonant()
word.add_consonant()
print(word.letters)

# run a number round and gen solution
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