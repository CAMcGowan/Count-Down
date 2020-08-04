import random
import numpy as np

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


# Runs 
word = WordRound()
word.add_vowel()
word.add_vowel()
word.add_vowel()
word.add_consonant()
word.add_consonant()
word.add_consonant()
word.add_consonant()
print(word.letters)