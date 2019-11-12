

#include "Bishop.h"
#include "Tile.h"
#include <cmath>

import Piece

class Bishop(Piece.Piece):
	
	""" The function creates the class variable of the Bishop
	Input- bishop's x, bishop's y, name(b or B)
	Output- none """
	def __init__(self, x, y, name):
		super().__init__(x, y, name)
		pass
	
	#Tile* , Board*
	""" The function checks if the movement to the destination tile is valid
	Input- tile to move to
	Output- if the move to the tile is valid """
	def checkMove(self, tile, board):
		moveValid = True

		#gets the offset of the x and y from current tile to destination tile
		xOffset = self.getX() - tile.getX()
		yOffset = self.getY() - tile.getY()

		#getsThe directio of the movement
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

		#checks if the incline is 1 and that it does not divide by zero
		if (yOffset != xOffset):
			#sets the move as an illegal move
			moveValid = False

		if (moveValid):
			i = 1
			while (i < xOffset):
				#checks if there is a piece between the current tile to destination tile
				if (board.getTile(self.getX() + i * xDirection, self.getY() + i * yDirection).getPiece()):
					moveValid = False
				i = i + 1

		return moveValid

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Bishop::~Bishop()
	{
	}"""

	""" The function changes the piece after the move
	Input- none 
	Output- none 
	void Bishop::afterMove()
	{

	}"""