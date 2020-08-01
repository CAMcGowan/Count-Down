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


# I need
# letters
# return letters
# Need to split vowels and consonants

class WordRound:
	# A number round
	def __init__(self):
		# Create the numbers based on weights
		self.letter_weights = [ ('A',15), ('B',2), ('C',3), ('D',6), ('E',21), ('F',2), ('G', 3),
								('H',2), ('I',13),  ('J',1), ('K',1), ('L',5), ('M',4), ('N',8), 
								('O',13), ('P',4), ('Q',1), ('R',9), ('S',9), ('T',9), ('U',5), 
								('V',1), ('W',1), ('X',1), ('Y',1), ('Z',1)]

		# Loop to create a weighted list
		self.letters_list = []
		for item, weight in self.letter_weights:
		    self.letters_list.extend( [item]*weight )
		self.letters_list = np.array(self.letters_list)	
		# List to store letters
		self.letters = []


	def add_letter(self):
		# Selecting a letter
		letter = random.choice(self.letters_list)
		# Index of target element
		idx = np.where(self.letters_list == letter)[0][0]
		# Remove letter from list
		self.letters_list = np.delete(self.letters_list, idx)
		# Store the letter
		self.letters.append(letter)



word = WordRound()
word.add_letter()
word.add_letter()
word.add_letter()
print(word.letters)


# letter = random.choice( letters )
