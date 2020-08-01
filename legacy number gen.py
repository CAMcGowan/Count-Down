	def add_small(self):
		# Find array length
		n = len(self.small_numbers)
		# Generate an index based on array length
		x = self.small_numbers[random.randint(0,n-1)]
		# Index of target element
		idx = np.where(self.small_numbers == x)[0]
		# Find and remove target element
		self.small_numbers = np.delete(self.small_numbers, idx)
		# store the number
		self.numbers.append(x)

	def add_big(self):
		# Find array length
		n = len(self.big_numbers)
		# Generate an index based on array length
		x = self.big_numbers[random.randint(0,n-1)]
		# Index of target element
		idx = np.where(self.big_numbers == x)[0]
		# Find and remove target element
		self.big_numbers = np.delete(self.big_numbers, idx)
		# store the number
		self.numbers.append(x)