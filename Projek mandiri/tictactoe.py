import random

TheBoard = {
	'top_L':'','top_M':'','top_R':'',
	'mid_L':'','mid_M':'','mid_R':'',
	'low_L':'','low_M':'','low_R':''
}


def printBoard(board):
	print(board['top_L'] + ' | ' + board['top_M'] + ' | ' + board['top_R'])
	print('--+--+--')
	print(board['mid_L'] + ' | ' + board['mid_M'] + ' | ' + board['mid_R'])
	print('--+--+--')
	print(board['low_L'] + ' | ' + board['low_M'] + ' | ' + board['low_R'])

turn = 'X'

player_score,com_score = 0,0
langkah_player = []
langkah_computer = ['top_M','top_R','mid_L','mid_R','low_L','low_M''top_L','mid_M','low_R']


while len([nilai for nilai in TheBoard.values() if nilai != ''])!= 9:
	print('top_L\ttop_M\ttop_R\nmid_L\tmid_M\tmid_R\nlow_L\tlow_M\tlow_R\n\n')
	print(f'\nyour score is {player_score}')
	print(f'com score is {com_score}')
	printBoard(TheBoard)
	print('\nTurn for ' + turn + '. Move on which space?' if turn == 'X' else 'computer is run')
	try:
		if turn == 'X':
			move = input()
			langkah_player.append(move)
			if move in langkah_computer:langkah_computer.remove(move)
		elif turn == 'O':
			move = random.choice(langkah_computer)
			langkah_computer.remove(move)
	except ValueError:
		print('langkah tidak sah !!!')
		break


	TheBoard[move] = turn 
	if turn == 'X':turn = 'O'
	elif turn == 'O':turn = 'X'

	## for x and x
	if TheBoard['top_L']==TheBoard['top_M']==TheBoard['top_R']=='X':
		player_score += 1
	elif TheBoard['low_L']==TheBoard['low_M']==TheBoard['low_R']=='X': 
		player_score += 1
	elif TheBoard['top_L']==TheBoard['mid_L']==TheBoard['low_L']=='X':
		player_score += 1
	elif TheBoard['top_R']==TheBoard['mid_R']==TheBoard['low_R']=='X':	
		player_score += 1
	elif TheBoard['top_L']==TheBoard['mid_M']==TheBoard['low_R']=='X':
		player_score += 1
	elif TheBoard['mid_L']==TheBoard['mid_M']==TheBoard['mid_R']=='X':
		player_score += 1
	elif TheBoard['top_M']==TheBoard['mid_M']==TheBoard['low_M']=='X':
		player_score += 1
	# # for O and O
	if TheBoard['top_L']==TheBoard['top_M']==TheBoard['top_R']=='O':
		com_score += 1
	elif TheBoard['low_L']==TheBoard['low_M']==TheBoard['low_R']=='O': 
		com_score += 1
	elif TheBoard['top_L']==TheBoard['mid_L']==TheBoard['low_L']=='O':
		com_score += 1
	elif TheBoard['top_R']==TheBoard['mid_R']==TheBoard['low_R']=='O':
		com_score += 1
	elif TheBoard['top_L']==TheBoard['mid_M']==TheBoard['low_R']=='O':
		com_score += 1
	elif TheBoard['mid_L']==TheBoard['mid_M']==TheBoard['mid_R']=='O':
		com_score += 1
	elif TheBoard['top_M']==TheBoard['mid_M']==TheBoard['low_M']=='O':
		com_score += 1
				
printBoard(TheBoard)
if player_score > com_score:print(f'player win\nscore : {player_score}')
elif player_score == com_score:print(f'draw\nplayer score : {player_score}\ncom score : {com_score}')
else:print(f'com win\nscore : {com_score}')