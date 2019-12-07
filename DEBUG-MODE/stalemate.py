import gen_moves
import print_board
import pieces


def stalemate(board, board_dict): #Returns true if no legal moves can be done, otherwise false
	black_count = 0
	white_count = 0
	black_stalemate = False
	white_stalemate = False

	for key, value in board_dict.items():
		if board[key[0]][key[1]] != '0':
			if board[key[0]][key[1]][1] == '1':
				white_count += len(value)
			elif board[key[0]][key[1]][1] == '2':
				black_count += len(value)


	if black_count == 0:
		black_stalemate = True
		print(black_count)
	elif white_count == 0:
		white_stalemate = True


board = print_board.gen_board()

# board[2][5] = 610
# board[3][5] = 110
# board[1][5] = 110
# board[1][6] = 110
# board[5][3] = 620
# board[7][3] = 0
# board[0][3] = 0
board_dict = gen_moves.gen_moves(board)

graveyard = []

stalemate(board, board_dict)