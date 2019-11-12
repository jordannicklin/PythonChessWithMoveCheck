ZERO_ASCII = 48
A_ASCII = 97
BOARD_SIZE = 8

#include "Board.h"
#include <iostream>

import Tile

class Board():
	""" The function creates the class variable of the Bishop
	Input- none
	Output- none """
	def __init__(self):
		"""self._tiles = [[Tile.Tile(0,0,0)]*BOARD_SIZE]*BOARD_SIZE
		#creates all of the tiles
		i = 0
		while (i < BOARD_SIZE - 1):
			i = i + 1
			j = 0
			while (j < BOARD_SIZE - 1):
				j = j + 1
				#creates tile in the place of i,j
				self._tiles[i][j] = Tile.Tile(j,i,None)#(j + A_ASCII, i + ZERO_ASCII, 0)"""

		self._tiles = []                                                           
		for i in range (0, BOARD_SIZE):                              
			new = []                 
			for j in range (0, BOARD_SIZE):   
				new.append( Tile.Tile(j,i))  
			self._tiles.append(new)

	""" The function delets all of the dynamic variables
	Input- none
	Output- none 
	Board::~Board()
	{
		#deletes all of the tiles
		for (i = 0 i < BOARD_SIZE i++)
		{
			for (j = 0 j < BOARD_SIZE j++)
			{
				#deletes tile in the place of i,j
				delete _tiles[i][j]
			}
		}
	}"""

	""" The function returns a tile in the place of inputed x,y
	Input- x,y of the tile to get 
	Output- tile in the place of x,y"""
	def getTile(self, x, y):
		#changes the char value to int
		#x -= A_ASCII
		#y -= ZERO_ASCII

		#returns tile in x and y
		#print(self._tiles[int(y)][int(x)])
		return self._tiles[int(y)][int(x)]