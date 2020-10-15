import countdown as cd
from tqdm import tqdm
import time

class Game():

	def play_word():
		word_round = cd.WordRound()
		for _ in range(7):
			choice = input('Vowel or Consonant? V/C')
			if choice == 'V':
				word_round.add_vowel()
			else:
				word_round.add_consonant()
			print(word_round.letters)

		print('')
		print('Final letters')
		print(word_round.letters)
		for i in tqdm(range(30)):
			time.sleep(1)
		print("Time's up")

	def play_number():
		number_round = cd.NumberRound()
		
		for _ in range(6):
			choice = input('Big or Small? B/S')
			if choice == 'B':
				number_round.add_big()
			else:
				number_round.add_small()
			print(number_round.nums)

		play = 'N'
		while play == 'N':
			number_round.change_target()
			print(number_round.target)
			play = input('Happy with target? Y/N')

		for i in tqdm(range(30)):
			time.sleep(1)
		print("Time's up")
		print('')
		print('Solution')
		s = number_round.solve()
		print(min(s, key=len))

	def standard_game():
		for _ in range(3):
			play_word()
			play_word()
			play_number()

	def custom_game():
		new_round = 'Y'

		while new_round == 'Y':
			game_round = input('Number or Words? N/W')
			if game_round == 'N':
				Game.play_number()
			else:
				Game.play_word()

			new_round = input('Play again? Y/N')


if __name__ == '__main__':
	print('Welcome to countdown!')
	play = input('Standard game, custom game or settings? S/C')

	if play == 'S':
		Game.settings()
	else:
		Game.custom_game()
