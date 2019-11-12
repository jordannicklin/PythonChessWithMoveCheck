
#include <cmath>

#include "Rook.h"
#include "Tile.h"

import Piece

class Rook(Piece.Piece):

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
		if (self.getX() > tile.getX()):
			xDirection = -1 
		else: 
			xDirection = 1
		if (self.getY() > tile.getY()):
			yDirection = -1
		else:
			yDirection = 1

		#gets the absolute value of the offsets
		xOffset = abs(xOffset)
		yOffset = abs(yOffset)

		#checks if the rock moved in a straight line (x or y moved and the other one didn't)
		if ((xOffset == 0 and yOffset != 0) or (xOffset != 0 and yOffset == 0)):
			moveValid = True

		#checks if the move is legal
		if (moveValid):
			#checks if the rook is moving on the x colom or y colom
			if (xOffset != 0):
				i = 1
				#checks if there is any pieces between source tile to destination tile
				while (i < xOffset):
					#checks if there is a piece in tile in the place of x,y
					if (board.getTile(self.getX() + i * xDirection, self.getY()).getPiece()):
						moveValid = False
					i = i + 1
			else:
				i = 1
				#checks if there is any pieces between source tile to destination tile
				while (i < yOffset):
					#checks if there is a piece in tile in the place of x,y
					if (board.getTile(self.getX(), self.getY() + i * yDirection).getPiece()):
						moveValid = False
					i = i + 1

		return moveValid

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Rook::~Rook()
	{
	}"""

	""" The function changes the piece after the move
	Input- none
	Output- none """
	def afterMove(self):
		pass