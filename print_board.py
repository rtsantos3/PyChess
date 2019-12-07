rows_cols = 8

row_letters = ['a','b','c','d','e','f','g','h']
row_letters_index = [row_letters.index(x) for x in row_letters]
board_layout = ['210', '310', '410', '510', '610', '410', '310', '210']

def gen_board():  #Sets start position for chess pieces

	board = ['0' for x in range(rows_cols)]
	for row in range(0, rows_cols):
		board[row] = ['0'] * (rows_cols)
		
		#Flag format: piece, color, has_moved(zero if not moved yet)
	for i in range(0, rows_cols):
		for j in range(0, rows_cols):
			#white
			board[6][j] = '110' #Pawn
			board[7][0] = '210' #Rook
			board[7][7] = '210' #Rook
			board[7][1] = '310' #Knight
			board[7][6] = '310' #Knight
			board[7][2] = '410' #Bishop
			board[7][5] = '410' #Bishop
			board[7][3] = '510' #Queen
			board[7][4] = '610' #King

			#maybe pwede ganito 
			#board[7][j] = map(int, [210, 310, 410, 510, 610, 410, 310, 210])
			#Black
			board[1][j] = '120' #Pawn
			board[0][0] = '220' #Rookr
			board[0][7] = '220' #Rook
			board[0][1] = '320' #Knight
			board[0][6] = '320' #Knight
			board[0][2] = '420' #Bishop
			board[0][5] = '420' #Bishop
			board[0][3] = '520' #Queen	
			board[0][4] = '620' #King

	return board

def print_board(board, graveyard):
	symbols =  {'0':'  ','12':"\u2659",'22':"\u2656",
				'32':"\u2658",'42':"\u2657",'52':"\u2655",'62':"\u2654",
				'11':"\u265F",'21':"\u265C",'31':"\u265E",
				'41':"\u265D",'51':"\u265B",'61':"\u265A",
				'71':' ', '72':' '}

	for i in row_letters:
		print('%7s' % i, end=' ')
	print(' ')
	print(' ')

	for idx_row, i in enumerate(board):
		print(-(idx_row - 8), end= " ")
		for idx_col, j in enumerate(i):
			piece = str(j)[:2]
			print('|',end=' ')
			print("%3s" % symbols[piece], end=' ')
			print('|', end=' ')
		print(' ')

		print(' ')

	for i in row_letters:
		print('%7s' % i, end=' ')
	print(' ')


	print('Pieces that are out:\n')
	for item in graveyard:
		piece_code = str(item)[:2]
		print("%2s" % symbols[piece_code], end=' ')
	print(' ')


	# for i_index, i in enumerate(board):
	# 	for j_index, j in enumerate(i):
	# 		print("%5d" % i_index, j_index, end=' ')
	# 	print(' ')
#works now



# def print_board(board):
# 	symbols =  {0:'  ',11:"\u2659",182:"\u2656",
# 				3:"\u2658",4:"\u2657",5:"'\u2655",6:"'\u2654",
# 				7:"'\u265F",8:"'\u265C",9:"'\u265E",
# 				10:"'\u265D",11:"'\u265B",12:"'\u265A"}

# 	for i in range(len(board)):
# 		print(-(i - 8), end=" ")
# 		for j in board[i]:
# 			# print('%3s' % symbols[j], end='', sep="")
# 			print('%3s' % board[j], end='', sep="")
# 		print(' ')
# 		print(' ')

# 	print(' ', end= '  ')
# 	for i in row_letters:
# 		print('%2s'% i, end=' ')

