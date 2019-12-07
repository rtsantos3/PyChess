import print_board
import pieces

def gen_moves(board): #Ouputs a list of moves per square w/c is used to check whether turn is legal or not.
	board_dict = {}

	for i, row in enumerate(board):
		for j, pc in enumerate(row):

			if pc == '0': #Skips the square if it's empty to save space
				continue
			

			elif pc != '0':

				piece = str(pc)[0]
				color = str(pc)[1]

				
				if piece == '1':
					board_dict[(i,j)] = pieces.pawn_move(board, pc, i, j) #Only en passant untested

				elif piece == '2':
					board_dict[(i,j)] = pieces.rook_move(board, color, i, j) #Fixed, needs to reinitialize movelist every
					#Fixed
				elif piece == '3':
					board_dict[(i,j)] = pieces.knight_move(board, color, i, j) #Fixed

				elif piece == '4':
					board_dict[(i,j)] = pieces.bishop_move(board, color, i, j) #Fixed

				elif piece == '5':
					board_dict[(i,j)] = pieces.queen_move(board, color, i, j) #Fixed

				elif piece == '6':
					board_dict[(i,j)] = pieces.king_move(board, board_dict, pc, i, j)


	return board_dict




# # Works now :)