

#include <stdio.h>

#include "Player.h"

class Player:

	""" The function creates the class variable of the player
	Input- none
	Output- none """
	def __init__(self):
		self._pieces = []
		self._king = None

	""" The function returns the king of the player
	Input- none
	Output- the king of the player"""
	def getKing(self):
		return self._king

	#Player* otherPlayer, Board*
	""" The function checks if there is a check on this player
	Input- other player, the game board
	Output- if there is a check """
	def checkCheck(self, otherPlayer, board):
		canEatKing = False

		i = 0
		#checks if all the pieces can eat the king
		while (i < len(otherPlayer._pieces) and not canEatKing):
			#checks if the piece in the place of i can eat the king
			canEatKing = otherPlayer._pieces[i].checkKing(self.getKing(), board)
			i = i + 1

		return canEatKing

	""" The function inserts a piece into the player piece
	Input- piece to insert
	Output- none """
	def insertPiece(self, piece):
		#inserts piece
		self._pieces.append(piece)

		#checks if the piece is a king
		if (piece.getType() == 'K' or piece.getType() == 'k'):
			#sets the king as inputed piece
			self._king = piece

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Player::~Player()
	{
		Piece* toDelete = 0

		#delets all the pieces
		for (i = 0 i < _pieces.size() i++)
		{
			#gets the piece
			toDelete = _pieces[i]

			#removes the piece from vector
			_pieces.erase(_pieces.begin() + i)

			#delets the piece
			delete toDelete
		}
	}"""