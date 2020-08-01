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



word = WordRound()
word.add_vowel()
word.add_vowel()
word.add_vowel()
word.add_consonant()
word.add_consonant()
word.add_consonant()
word.add_consonant()
print(word.letters)


# letter = random.choice( letters )
