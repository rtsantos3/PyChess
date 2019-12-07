pieces_to_ignore = ['0','711','721'] #Pieces to be ignored by pieces except pawns. Includes empty squares

def is_enemy(color, board_value): #Compares integer identities
	board_color = str(board_value)[1]

	if board_color == color:
		return False
	else:
		return True



def pawn_move(board, pc, i, j):
	movelist = []
	moveset = [[1,0],[2,0],[1,1],[1,-1]] #Made it into a 1 dimensional list so it can be reversed easily

	color = pc[1]
	move_flag = pc[2]
	if color == "1": #If white, just reverses the signs.

		moveset = [[moveset[i][j] * -1 
					for j in range(len(moveset[i]))] 
					for i in range(len(moveset))]

	front = []
	doub_front = []
	front_diags = []
	sides = []

	#Define fronts, (single and double)
	front_i = i + moveset[0][0]
	doub_front_i = i + moveset[1][0]

	if 0 <= front_i < 8:
		front = [front_i, j]
	if 0 <= doub_front_i < 8:
		doub_front = [doub_front_i, j]


	#Define diags
	for x in range(2,4):
		new_i = i + moveset[x][0]
		new_j = j + moveset[x][1]
		if 0 <= new_i < 8 and 0 <=new_j <8:
			front_diags.append([new_i, new_j]) #Works now

	#Define sides
	side_a = j - 1
	side_b = j + 1
	if 0 <= side_a < 8:
		sides.append([i, side_a])
	if 0 <= side_b < 8:
		sides.append([i, side_b]) #Works now

	#Front moveset
	if board[front[0]][front[1]] == '0':
		movelist.append(front)
		if board[doub_front[0]][doub_front[1]] == '0' and move_flag == '0':
			movelist.append(doub_front) #Works

	#Diag moveset
	for items in front_diags:
		board_value = board[items[0]][items[1]]
		if board_value != '0' and is_enemy(color, board_value) == True:
			movelist.append(items) #Works

	#En passant
	# en_passant = [x for x in front_diags
	# 				for y in sides
	# 				if x[1] == y[1]
	# 				if all([board[y[0]][y[1]] != '0', board[y[0][y[1]][0] == '1']] == True)
	# 				]

	# print("en_passant of:", i, j, en_passant)

	# # for items in en_passant:
	# # 	print('en_passant:',en_passant)
	# # 	board_value = str(board[items[0]][items[1]])
	# # 	if board_value[0] == "1" and is_enemy(color, board_value) == True:
	# # 		if prev_board[-1][0] == board_value:
	# # 			movelist.append(items)

	return movelist

def knight_move(board, color, i, j):
	movelist = []
	moveset = [[1,2],[-1,2],[1,-2],[-1,-2],
				[2,1],[-2,1],[2,-1],[-2,-1]]

	# if piece != '0':
	# 	color = str(piece)[1]

	for moves in moveset:

		new_i = i + moves[0]
		new_j = j + moves[1]
		if 0 <= new_i < 8 and 0 <= new_j < 8:
			board_value = board[new_i][new_j]
			
			if board_value in pieces_to_ignore:
				movelist.append([new_i,new_j])
			elif board_value != '0':
				if is_enemy(color, board_value) == True:
					movelist.append([new_i,new_j])



	return movelist


def bishop_move(board, color, i, j):
	listmoves = []
	orig_i = i
	orig_j = j


	listmoves.append(move_diag1(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_diag2(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_diag3(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_diag4(board, color, orig_i, orig_j, movelist=[]))

	listmoves = [i
				for item in listmoves
				for i in item] #Flattens list to 1 d only

		#Returns 1 dimensional list so it can be read by other functions without looping
	return listmoves


def move_diag1(board, color, i, j, movelist=[]):
	new_i = i + 1
	new_j = j + 1

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_diag1(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist



def move_diag2(board, color, i, j, movelist=[]):
	new_i = i + 1
	new_j = j - 1

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_diag2(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist

# 	moves = [[1,0],[0,1],[-1,0],[0,-1]]

def move_diag3(board, color, i, j, movelist=[]):
	new_i = i - 1
	new_j = j + 1

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_diag3(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist


def move_diag4(board, color, i, j, movelist=[]):
	new_i = i - 1
	new_j = j - 1


	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]

		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_diag4(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist




def rook_move(board, color, i, j):

	listmoves = []
	orig_i = i
	orig_j = j
	# color = str(piece)[1]

	listmoves.append(move_down(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_right(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_up(board, color, orig_i, orig_j, movelist=[]))
	listmoves.append(move_left(board, color, orig_i, orig_j, movelist=[]))

	listmoves = [i
				for item in listmoves
				for i in item] #Flattens list to 1 d only

	#Returns 1 dimensional list
	return listmoves


def move_down(board, color, i, j, movelist=[]):
	new_i = i + 1
	new_j = j + 0

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_down(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist


def move_right(board, color, i, j, movelist=[]):
	new_i = i + 0
	new_j = j + 1

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_right(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist

# 	moves = [[1,0],[0,1],[-1,0],[0,-1]]

def move_up(board, color, i, j, movelist=[]):
	new_i = i - 1
	new_j = j + 0

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]
		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_up(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist
	else:
		return movelist


def move_left(board, color, i, j, movelist=[]):
	new_i = i + 0
	new_j = j - 1
	board_value = board[new_i][new_j]

	if 0 <= new_i < 8 and 0 <= new_j < 8:

		board_value = board[new_i][new_j]

		if board_value in pieces_to_ignore:
			movelist.append([new_i, new_j])
			return move_left(board, color, new_i, new_j, movelist)
		elif board_value != '0':
			if is_enemy(color, board_value) == True:
				movelist.append([new_i, new_j])
				return movelist
			else: #If same color
				return movelist

	else:
		return movelist


def queen_move(board, color, i, j):

	listmoves = []
	orig_i = i
	orig_j = j


	listmoves.append(bishop_move(board, color, orig_i, orig_j))
	listmoves.append(rook_move(board, color, orig_i, orig_j))

	listmoves = [i
				for item in listmoves
				for i in item] #Flattens list to 1 d only

	#returrns 1 dimensional list
	return listmoves


def king_move(board, board_dict, pc, i, j):
	movelist = []
	moveset = [[0,1],[1,1],[1,0],
				[0,-1],[1,-1],[-1,-1],
				[-1,0], [-1,-1]]

	color = pc[1]
	for moves in moveset:
		new_i = i + moves[0]
		new_j = j + moves[1]

		if 0 <= new_i < 8 and 0 <= new_j <8:
			coords = [new_i,new_j]
			
			for keys in board_dict.keys(): #kaso this would iterate over the entirety of the key list, so inefficient siya, especially if it's done every turn
				if coords in board_dict[keys]: #if it leads to check

					continue
				else:
					board_value = board[new_i][new_j]
					if coords not in movelist:
						if board_value in pieces_to_ignore:
						 	movelist.append(coords)
						else:
							if is_enemy(color, board_value) == True:
								movelist.append(coords)

			
	if pc[2] == '0': #If king hasn't moved
		#Kingside
		if board[i][7][0] == '2' and board[i][7][2] == '0':
		 #If rook is in square and hasn't moved
			if board[i][5] == '0' and board[i][6] == '0':  #If all squares between the rook and king are empty #Rook, King side
				movelist.append([i, 6]) #Adds castle kingside
		#Queenside
		if board[i][0][0] == '2' and board[i][0][2] == '0': #If rook is in square and hasn't moved
			if all([board[i][1] == '0', board[i][2] == '0', board[i][3] == '0']):  #Rook, queenside
				movelist.append([i, 2]) #Adds castle queenside
	
	return movelist



