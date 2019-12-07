import print_board
import pieces
import datetime
import os
import gen_moves
import re



def print_menu():
	
	while True:
		print("%5s" % 'Python Chess \n')
		print("%5s" % 'By Russel Santos \n')
		print("%5s" % 'Please choose options below:\n')
		print("%5s" % "1. New Game \n")
		print("%5s" % "2. Load Game \n")
		print("%5s" % "3. Exit \n")



		choice = input("Please Choose From options above \n")

		if choice == "1":
			board = print_board.gen_board()
			game_start(board, next_turn="white")

		elif choice == "2":
			board, next_turn =load_game()
			game_start(board, next_turn)

		elif choice == "3":
			print("Thank you for opening my app!")
			exit()
		else:
			print("Invalid selection. Try again!")
			continue

def game_start(board, next_turn, graveyard=[]):
	board_dict = {} #Contains all legal moves
	board_dict = gen_moves.gen_moves(board) #initialize board moves
	prev_board=list()
 #Keeps previous board states, so it can return if needed

	 #Keeps previous d state #I don't know why, but it works lol
	while True: #If not checkmate, then returns here
		
		temp_board = [] #I typecasted it into tuples because board states couldn't be saved without altering previous board states.
		for lists in board:
			temp_board.append(tuple(lists))

		prev_board.append(tuple(temp_board))

		while True: #

			board_dict = gen_moves.gen_moves(board) #This  initializes the moveset.

			board = turn(board, next_turn, board_dict, graveyard)
			
			board_dict = gen_moves.gen_moves(board) #This is for checking if the kings are in check.
			
			Black_check_state, White_check_state, Checkmate_state = check_if_check(board, board_dict)
			print('Check values:' Black_check_state, White_check_state, Checkmate_state)

			if next_turn == "black":
				if Black_check_state == True:
					print('Move leads to check. Try again!')
					board = [list(item) for item in prev_board[-1]] #Returns board to previous state if invalid turn
					continue
			
			elif next_turn == "white":
				if White_check_state == True:
					print('Move leads to check. Try again!')
					board = [list(item) for item in prev_board[-1]] #Returns board to previous state if invalid turn
					continue

			if Checkmate_state == True:
				end_game(next_turn)
				print_menu()
				#Save to high score haha

			if stalemate(board, board_dict) == True or threefold_rep(board, prev_board) == True: #Draw conditions
				end_game(next_turn, draw=True)
				print_menu()

			else:
				next_turn = current_turn(next_turn)
				break


			


def current_turn(current):
	if current == "white":
		return "black"
	else:
		return "white"

def parse_coords(selection):
	row_letters = ['a','b','c','d','e','f','g','h']
	row_letters_index = [row_letters.index(x) for x in row_letters]


	i = 8 - int(selection[1])  #This simply reverses the notation, since the matrix counts from top to down.
	j = row_letters.index(selection[0]) #This converts letters to their index
	return i, j	 #works properly now


def turn(board, next_turn, board_dict, graveyard): #This justchecks if tama yung turn and outputs the board



	if next_turn == 'white': #Removes ghost pawns from play.
		for row, items in enumerate(board):
			for col, pc in enumerate(items):
				if pc == '711':
					board[row][col] = '0'
	elif next_turn == 'black':
		for row, items in enumerate(board):
			for col, pc in enumerate(items):
				if pc == '721':
					board[row][col] = '0'


	while True:
		print_board.print_board(board, graveyard)
		print(next_turn, "'s turn\n")
		i1, j1, i2, j2 = turn_input(board, next_turn)

		if board[i1][j1] == '0':
			print("board selection is empty, try again!")
			continue #If selection is empty

		else:
			color = board[i1][j1][1]
			piece = board[i1][j1][0]
			print(color)
			print(piece)
			if next_turn == "white": #Checks if wrong color selected
				if color != "1":
					print('Wrong color. Try again!')
					continue
			elif next_turn == "black":
				if color != "2":
					print('Wrong color. Try again!')
					continue

			else:
				break


		board_pc = board[i1][j1]

		#Check if move is in board_dict (if move is legal)
		if [i2, j2] in board_dict[(i1,j1)]: #Error catching is in gen_moves already, which checks if move is legal or not.

			if board_pc[0] == '6' and board_pc[2] == '0': #Castling, catches instance if king has moved already.


				if j2 == 6:
					board = castle(board, color, side="kingside")
				elif j2 == 2:
					board = castle(board, color, side="queenside")
				return board


			if (board_pc)[2] == "0": #Changes has moved flag on piece.
				board_pc = has_moved(board_pc)
			



			if board_pc[0] == '1': #Special cases for pawn
				print('pawn selected')
				if any([i2 == 0, i2 == 7]): #Upgrades rank if pawn reaches end of rows
					user_prompt = input('Upgrade the pawn to which piece?(Q/K)\n')

					if user_prompt.lower() == "q": #Upgrades piece to queen
						board[i2][j2] = "5"+color+"1"
						board[i1][j1] = '0'
					elif user_prompt.lower() == "k": #Upgrades piece to knight
						board[i2][j2] = "3"+color+"1"
						board[i1][j1] ='0'
					return board


				if i1 == 1 or i1 == 6: #If pawn moves 2 ranks
					print('does it reach here? En passant')
					if any([i2 == 3, i2 == 4]):
						print('does it reach here? En passant2')
						

						if i2 == 4:

							print('does it reach here? En passant3')
							print(i2, j2)
							board[5][j2] = '711'
							print(board[4])
					
						elif i2 == 3:

							print('does it reach here? En passant4')
							print(board[i1][j1])
							board[2][j2] = '721'
							print(board[5])
							#Create an attackable ghost pawn

			if board[i2][j2] == '0':
				board[i2][j2] = board_pc
				board[i1][j1] = '0'
				return board


			else: #If an enemy square:

				if board[i1][j1][0] == '1':
					if board[i2][j2] == '711' or board[i2][j2] == '721': #If ghost pawn is targetted
						if i2 == 2: #Removes both ghost pawns and normal pawns
							board[3][j2] = '0'
							board[2][j2] = '0'
							graveyard.append('121')

						if i2 == 5:
							board[4][j2] = '0'
							board[5][j2] = '0'
							graveyard.append('111')

				graveyard.append(board[i2][j2])
				board[i2][j2] = board_pc
				board[i1][j1] = '0'
				return board


	


def has_moved(board_pc):
	moved_pc = board_pc[0:2] + '1'
	return moved_pc
	#Works


def check_if_check(board, board_dict):
	#Format is black check, white check, checkmate
	white_king = []
	black_king = []

	Black_check_state = False
	White_check_state = False
	Checkmate_state = False

	for row_idx, row in enumerate(board): #Retrieves indices of white and black king.
		for col_idx, pc in enumerate(row):
			if pc[0] == "6": #If piece is a king
				if pc[1] == "1": #If piece is white 
					white_king = [row_idx, col_idx]

				elif pc[1] == "2":
					black_king = [row_idx, col_idx]

	for keys in board_dict.keys(): #Iterates over all board_dict states to check if king square is within attacking distance.
		if white_king in board_dict[keys]:
			White_check_state = True
			if checkmate_sqs(board, board_dict,white_king[0],white_king[1]) == True: # Checks if there are no turns left and own pieces cannot block the king's path
				Checkmate_state = True

		elif black_king in board_dict[keys]:
			Black_check_state = True
			if checkmate_sqs(board, board_dict,black_king[0],black_king[1]) == True:
 				Checkmate_state = True



	return Black_check_state, White_check_state, Checkmate_state

#Works

def checkmate_sqs(board, board_dict, i, j):
	surr_sqs = [[0,1],[1,1],[1,0],
			[0,-1],[1,-1],[-1,-1],
			[-1,0], [-1,-1]]

	surrounding_squares = []

	legal_move_count = 0

	for items in surr_sqs:
		new_i = i + items[0]
		new_j = j + items[1]
		print('surr_sqs',new_i, new_j)

		if 0 <= new_i < 8 and 0 <= new_j <8:
			surrounding_squares.append([new_i, new_j])


	for keys in board_dict.keys():
		for squares in surrounding_squares:
			if board[keys[0]][keys[1]][1] == board[i][j][1]: #If they're the same color
				print(keys, squares, legal_move_count)
				if squares in board_dict[keys]:
					legal_move_count += 1 #This means that the squares can be moved upon or blocked by own pieces.
	if legal_move_count == 0: 
		return True
	return False






def turn_input(board,next_turn):
	while True:
		selection = []
		target = []

		turn_input = input("Please input your turn: \n")

		if re.match('^[a-hA-H][1-8][a-hA-H][1-8]$', turn_input) != None: #just implement regex to check format is the ff: /w/d/w/d
			i1, j1 = parse_coords(turn_input.lower()[:2])
			i2, j2 = parse_coords(turn_input.lower()[2:4])
			break

		else:
			if turn_input.lower() == "save":
				save_game(board, next_turn)

			if turn_input.lower() == "exit":
				prompt = input("Exit the game?(Y/N)\n")
				if prompt.lower() == "y":
					print_menu()
				else:
					continue


			else:		
				print('Please enter your turn in the following format: (selection square)(target square)')
				continue


	return i1, j1, i2, j2
	#Returns properly




def end_game(current_turn, draw=False):
	save_stats = open('chess_stats.txt', "a+")
	date = str(datetime.datetime.now())
	line1 = ""
	if draw == True:
		print('Game is a Draw!')
		line1 = date + ' | Game Draw'+ "\n"
	
	else:
		print(current_turn, " is the Winner!")
		line1 = date + ' | Game Winner:' + current_turn + "\n"


	save_stats.write(line1+'\n')

	save_stats.close()


def save_game(board, current_turn):

	save_files_folder = os.listdir('save/')

	while True:

		save_file = input('Please input save file here: \n')
		save_file = save_file + '.txt'
		if save_file in save_files_folder:
			usr_prompt = input('Save file exists. Overwrite?(Y/N)\n')
			if usr_prompt.lower() == 'y':
				break
			else:
				print("Here's a list of save files:\n")
				for items in save_files_folder:
					print(items,'\n')

				continue
		else:
			break


	out = open('save/%s' % save_file, 'w+')
	curr_turn = 'Current_turn:' + current_turn + '\n'
	out.write(curr_turn)

	for rows in board:
		line = ""
		for items in rows:
			line = line + items + '\t'

		out.write(line + '\n')

	while True:
		print("Save successful!")
		usr_prompt = input('Continue game?(Y/N)\n')
		if usr_prompt.lower() == "y":
			out.close()
			game_start(board, current_turn)
		else:
			out.close()
			print_menu()



def load_game():
	save_files = os.listdir('save/')

	while True:
		try:

			board = []
			current_turn = ''
			print('Current saved games: \n')
			for items in save_files:
				print(items, '\n')

			load_input = input('Please choose a file from the list:\n')
			if load_input in save_files:
				with open('save/%s' % load_input, 'r') as sf:
					current_turn = sf.readline().rstrip().split(':')[1] #Works, gets the last turn

					for lines in sf.readlines():
						matrix = list(lines.rstrip().split('\t'))
						board.append(matrix)


				print_board.print_board(board, graveyard=[])
				print('\n')
				while True:
					confirm = input('Confirm selection? (Y/N)')
					if confirm.lower() == 'y':
						game_start(board, current_turn)
						break
					elif confirm.lower() == 'n':
						break
					else:
						continue
			else:
				print("Save file not in directory. Try again!")
				continue
		except IndexError: #Means that the file is not formatted and is not recognized.
			print('File format not recognized. Try again!')
			continue

	exit()


def castle(board, color, side):
	if side == "kingside":
		if color == "1":
			board[7][4] = "0"
			board[7][6] = "611" #King castle
			board[7][7] = "0"
			board[7][5] = "211" #Rook kingside

		elif color == "2":
			board[0][4] = "0"
			board[0][6] = "621" #King castle
			board[0][7] = "0"
			board[0][5] = "221" #Rook kingside

	elif side == "queenside":
		if color == "1":
			board[7][4] = "0"
			board[7][2] = "611" #King castle
			board[7][0] = "0"
			board[7][3] = "211" #Rook kingside

		elif color == "2":
			board[0][4] = "0"
			board[0][2] = "621" #King castle
			board[0][0] = "0"
			board[0][3] = "221" #Rook kingside

	return board

#tested now. Works //



def stalemate(board, board_dict): #Returns true if no legal moves can be done, otherwise false
	black_count = 0
	white_count = 0

	for key, value in board_dict.items():
		if board[key[0]][key[1]] != '0':
			if board[key[0]][key[1]][1] == '1':
				white_count += len(value)
			elif board[key[0]][key[1]][1] == '2':
				black_count += len(value)


	if black_count == 0 or white_count == 0:
		return True

	return False

def threefold_rep(board, prev_board):

	temp_board = []
	for lists in board:
		temp_board.append(tuple(lists)) #Typecasted it to tuple because I couldn't make the list form to work without errors.

	rep_count = 0
	if temp_board in prev_board: #3fold repetition 

		for items in prev_board:
			if board == items:
				rep_count += 1
		if rep_count == 3:
			return True


	return False
