

#include "Knight.h"
#include "Tile.h"
#include <cmath>

import Piece

class Knight(Piece.Piece):

	""" The function creates the class variable of the Bishop
	Input- bishop's x, bishop's y, name(b or B)
	Output- none """
	def __init__(self, x, y, name):
		super().__init__(x, y, name)
		pass

	#Tile* tile, Board*
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

		#checks if the one of the offsets is 1 and that the other one is 2
		if ((yOffset == 2 and xOffset == 1) or (xOffset == 2 and yOffset == 1)):
			moveValid = True

		#checks if there is a piece in the way
		#xDirection = (getX() > tile.getX()) if -1 : 1
		#yDirection = (getY() > tile.getY()) if -1 : 1

		"""if (moveValid)
		{
			if (xOffset == 2)
			{
				if (board.getTile(getX() + 1 * xDirection, getY()).getPiece())
				{
					moveValid = False
				}
			}
			else
			{
				if (board.getTile(getX(), getY() + 1 * yDirection).getPiece())
				{
					moveValid = False
				}
			}
		}"""

		return moveValid

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Knight::~Knight()
	{
	}"""

	""" The function changes the piece after the move
	Input- none
	Output- none 
	void Knight::afterMove()
	{

	}"""