import itertools
from colorama import Fore, Back, Style, init

init()

def choose_size():
	wrong_size = True
	while wrong_size == True:
		size_input = input('Please choose the size of the game (2 to 9): ')
		try:
			game_size = int(size_input)
		except ValueError:
			print('Wrong input. Pick a number between 3 and 10')
		else:
			game_size = int(size_input)
			if game_size < 2 or game_size > 9:
				print('Wrong input. Pick a number between 3 and 10')
			else:
				wrong_size = False
	return game_size

def reset_game_board(size):
	game_board = []
		
	for ii in range(size):
		aux = []
		for jj in range(size):
			aux.append('0')
		game_board.append(aux)
	
	print(Fore.BLUE + Back.WHITE + Style.BRIGHT + 'New Board:' + Style.RESET_ALL)
	
	s = ''
	for i in range(1,size+1):
		s += Back.WHITE + Fore.BLACK + Style.NORMAL + '    ' + str(i)
	print(s + '  ' + Style.RESET_ALL)

	for count, ii in enumerate(game_board):
		row_count = ''
		row_count = Back.WHITE + Fore.BLACK + str(count+1)
		print(row_count + ' ', Back.BLACK + str(ii) + Style.RESET_ALL)

	return game_board

def play(current_game, row, col, mark):

	print(Fore.BLUE + Back.WHITE + Style.BRIGHT + Style.NORMAL + 'Current Board:' + Style.RESET_ALL)
	row = row - 1
	col = col - 1
	if current_game[row][col] == '0':
		current_game[row][col] = mark


		s = ''
		for i in range(1,len(current_game)+1):
			s += Back.WHITE + Fore.BLACK +  '    ' + str(i)		
		print(s + '  ' + Style.RESET_ALL)

		for count, ii in enumerate(current_game):
			colored_row = ''
			for item in ii:
				if item == '0':
					colored_row += '     '
				elif item == 'O':
					colored_row += Fore.GREEN + Style.BRIGHT + item + '    ' + Style.RESET_ALL
				else:
					colored_row += Fore.RED + Style.BRIGHT + item + '    ' + Style.RESET_ALL

			print(Back.WHITE + Fore.BLACK + str(count+1) + '  ' + Style.RESET_ALL, colored_row)
			
	else:

		print(Back.RED + Fore.WHITE + 'Error: Place already taken' + Style.RESET_ALL)
		return

	return current_game

def win_hor(current_game):
	
	for row in current_game:
		row_winner = False
		if row.count(row[0]) == len(row) and row[0] != '0':
			row_winner = True
			break
	
	return row_winner

def win_ver(current_game):
	
	for col in range(len(current_game)):
		col_winner = False
		check = []
		for row in current_game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != '0':
			col_winner = True
			break

	return col_winner

def win_diag(current_game):
	diag_winner = False
	diag1 = []
	diag1_winner = False
	for ii in range(len(current_game)):
		diag1.append(current_game[ii][ii])

	if diag1.count(diag1[0]) == len(diag1) and diag1[0] != '0':
		diag1_winner = True

	diag2 = []
	diag2_winner = False
	for col, row in enumerate(reversed(range(len(current_game)))):
		diag2.append(current_game[row][col])

	if diag2.count(diag2[0]) == len(diag2) and diag2[0] != '0':
		diag2_winner = True

	if diag1_winner == True or diag2_winner == True:
		diag_winner = True

	return diag_winner

def no_win(current_game, game_size):
	no_winner = False
	count = 0
	for ii in range(len(current_game)):
		for jj in range(len(current_game)):
			if current_game[ii][jj] != '0':
				count += 1
			
	if count == game_size ** 2:
		no_winner = True

	return no_winner

def check_winner(current_game):
	
	row_winner = win_hor(current_game)
	col_winner = win_ver(current_game)
	diag_winner = win_diag(current_game)
	
	game_won = False
	if row_winner == True or col_winner == True or diag_winner == True:
		game_won = True

	return game_won

def main():
	game_size = choose_size()
	current_game = reset_game_board(game_size)
	game_won = False
	player_turn = itertools.cycle([1, 2])

	while game_won == False:
		player = next(player_turn)

		if player == 1:
			mark = 'O'
		else:
			mark = 'X'

		place_taken = True
		while place_taken ==True:		
			
			wrong_row_choice = True
			while wrong_row_choice == True:
				row_choiceInput = input('Player {}, choose row: '.format(player))
				try:
					row_choice = int(row_choiceInput)
				except:
					print('Please enter a row choice between 0 and {}'.format(game_size))
				else:
					row_choice = int(row_choiceInput)
					if row_choice < 1 or row_choice > game_size + 1:
						print('Please enter a row choice between 0 and {}'.format(game_size))
					else:
						wrong_row_choice = False

			wrong_col_choice = True
			while wrong_col_choice == True:
				col_choiceInput = input('Player {}, choose column: '.format(player))
				try:
					col_choice = int(col_choiceInput)
				except :
					print('Please enter a column choice between 0 and {}'.format(game_size))
				else:
					col_choice = int(col_choiceInput)
					if col_choice < 1 or col_choice > game_size + 1:
						print('Please enter a column choice between 0 and {}'.format(game_size))
					else:
						wrong_col_choice = False

			if current_game[row_choice - 1][col_choice - 1] != '0':
				print('Place already taken')
			else:
				place_taken = False

		play(current_game,row = row_choice, col = col_choice, mark = mark)
		
		game_won = check_winner(current_game)
		no_winner = no_win(current_game, game_size)

		if game_won == True:
			print('Congratulations Player {}! You won!!!'.format(player))
			return

		if no_winner == True:
			print('No one won :(. It\'s a draw')
			return
	return

main()

play_again = True
while play_again == True:
	ask = input('Do you want to play again? (Y/N): ')
	ask = ask.lower()
	if ask != 'y' and ask != 'n':
		print('Sorry, didn\'t get that. Please respond Y or N.')
	elif ask == 'y':
		main()
	else:
		print('Thank you for playing, Bye!')
		exit()