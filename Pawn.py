#include "Pawn.h"
#include "Tile.h"

import Piece

class Pawn(Piece.Piece):

	# Piece(x, y, name):
	# char char char
	""" The function creates the class variable of the Bishop
	Input- bishop's x, bishop's y, name(b or B)
	Output- none """
	def __init__(self, x, y, name):
		self._firstMove = True
		super().__init__(x, y, name)
		pass

	#Tile*, Board*
	""" The function checks if the movement to the destination tile is valid
	Input- tile to move to
	Output- if the move to the tile is valid """
	def checkMove(self, tile, board):
		moveValid = False

		#gets the offset of the x and y from current tile to destination tile
		xOffset = self.getX() - self.getX()
		yOffset = self.getY() - tile.getY()

		#gets the movement direction
		if self.isWhite():
			direction = -1
		else:
			direction = 1

		#gets offsets
		if xOffset < 0:
			xOffset =  xOffset * -1
		if not self.isWhite():
			yOffset = yOffset * -1

		#checks if the movemnet is legal
		if (((xOffset == 0 and not(tile.getPiece())) or (xOffset == 1 and tile.getPiece())) and (yOffset == 1 or (yOffset == 2 and self._firstMove and not(tile.getPiece())))):
			moveValid = True

		#checks if there is a piece in the way
		if (yOffset == 2 and board.getTile(self.getX(), self.getY() + direction).getPiece()):
			moveValid = False

		return moveValid

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Pawn::~Pawn()
	{
	}"""

	""" The function changes the piece after the move
	Input- none
	Output- none """
	def afterMove(self):
		self._firstMove = False