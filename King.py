

#include "King.h"
#include "Tile.h"

#include <cmath>

import Piece

class King(Piece.Piece):

	# Piece(x, y, name):
	# char char char
	""" The function creates the class variable of the Bishop
	Input- bishop's x, bishop's y, name(b or B)
	Output- none """
	def __init__(self, x, y, name):
		super().__init__(x, y, name)
		pass

	#Tile*, Board*
	""" The function checks if the movement to the destination tile is valid
	Input- tile to move to
	Output- if the move to the tile is valid """
	def checkMove(self, tile, board):
		moveValid = False 

		#gets the offset of the x and y from current tile to destination tile
		xOffset = self.getX() - tile.getX()
		yOffset = self.getY() - tile.getY()

		#gets the absolute value of the offsets
		xOffset = abs(xOffset)
		yOffset = abs(yOffset)

		#checks if the the offset of x and y is 0 or 1 and that at least one of them is 1
		if ((yOffset >= 0 and yOffset <= 1) and (xOffset >= 0 and xOffset <= 1) and (yOffset == 1 or xOffset == 1)):
			moveValid = True

		return moveValid

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	King::~King()
	{
	}"""

	""" The function changes the piece after the move
	Input- none
	Output- none """
	def afterMove(self):
		pass