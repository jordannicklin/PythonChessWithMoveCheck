#pragma once

#include "Tile.h"

class Tile:
	
	# char ,char ,Piece*
	""" The function creates the class variable of the Bishop
	Input- bishop's x, bishop's y, piece to set on tile
	Output- none """
	def __init__(self, x, y, piece = None):
		self._x = x
		self._y = y
		self._piece = piece

	""" The function returns the piece on the tile
	Input- none
	Output- piec of the tile """
	def getPiece(self):
		return self._piece

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Tile::~Tile()
	{

	}"""

	#Piece*
	""" The function sets inputed piece as tile piece
	Input- piece to set
	Output- none """
	def setPiece(self, piece):
		self._piece = piece

	""" The function returns the x of the tile
	Input- none
	Output- the x of the tile """
	def getX(self):
		return self._x

	""" The function returns the x of the tile
	Input- none 
	Output- none """
	def getY(self):
		return self._y