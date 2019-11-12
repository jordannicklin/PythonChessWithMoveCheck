

#include <stdio.h>
#include <ctype.h>

#include "Piece.h"
#include "Tile.h"
#include "Board.h"
#include "Player.h"

MIN_X = '0'
MAX_X = '7'

MIN_Y = '0'
MAX_Y = '7'

from enum import Enum

class Piece:

	class int_message(Enum):
		LEGAL_MOVE = 1
		LEGAL_MOVE_CREATE_CHECK = 2
		NO_PIECE_IN_SOURCE = 3
		PIECE_IN_DES = 4
		CHECK_AFTER_MOVE = 5
		ILLEGAL_INDEX = 6
		INCORRECT_MOVEMENT = 7
		SRC_TILE_IS_DST_TILE = 8

	""" The function creates the dynamic variabels
	Input- none
	Output- none """
	def __init__(self, x, y, type):
		self._y = y
		self._x = x
		self._type = type

	""" The function returns if the piece is white or black
	Input- none
	Output- if the piece is white """
	def isWhite(self):
		return ((self._type.upper()) == self._type)

	""" The function returns the type of the piece
	Input- none
	Output- the type of the piece """
	def getType(self):
		return self._type
	
	#Tile*, Board*
	""" The function move the piece to inputed tile
	Input- distanation tile
	Output-none """
	def move(self, tile, board):
		#get source tile
		tileSrc = board.getTile(self._x, self._y)

		#sets that there is no piece on source tile 
		tileSrc.setPiece(0)

		#sets the x and y to destination tile
		self._x = tile.getX()
		self._y = tile.getY()

		#sets piece on destination tile as this piece
		tile.setPiece(self)
		self.afterMove()

	#char, char
	""" The fuction check if inputed x and y is in the board
	Input- x and y to check
	Output- if the x and y is in the board"""
	def checkInBoard(self, x, y):
		#checks if the x or -y is out of the range
		return (x >= MIN_X and x <= MAX_X) and (y >= MIN_Y and y <= MAX_Y)

	#char, char, Board*
	""" The functions checks the movment of the piece and return if it is valid
	Input- destination x, destination y, board """
	def checkDistanation(self, x, y, board):
		#checks if the destination x and y are in the board
		if (not(self.checkInBoard(x, y))):
			return 5

		#gets tile in the destination x and y
		tile = board.getTile(x, y)

		#checks if the destination tile has a piece of the current player
		if (self.checkPieceOnDst(tile)):
			return 3

		#checks if the move is legal
		if (self.checkMove(tile, board)):
			return 0

		#returns that the move is illegal
		return 6

	#Tile*
	""" The function check if the piece on the is from player as this piece
	Input- destination tile
	Output- if the two piece is from the same player """
	def checkPieceOnDst(self, disTile):
		#checks if theres a piece on the tile
		if (disTile.getPiece()):
			#retutns if both pieces are from the same player
			return (disTile.getPiece().isWhite() == self.isWhite())
		else:
			return False

	""" The function delets all of the dynamic variabels
	Input- none
	Output- none 
	Piece::~Piece()
	{
	}"""

	""" The functions returns the x of the piece
	Input- none
	Output- the x of the piece """
	def getX(self):
		return self._x

	""" The functions returns the y of the piece
	Input- none
	Output- the y of the piece """
	def getY(self):
		return self._y

	#Piece* , Board*
	""" The functions checks if the piece can eat the inputed king
	Input- the king, the board 
	Output- if the piece can eat the king """
	def checkKing(self, king, board):
		#get the tile of the king
		kingTile = board.getTile(king.getX(), king.getY())
		
		#checks if the piece can move to the tile of the king
		return self.checkMove(kingTile, board)

	#Player* , Player* , Board* , Tile*
	""" The function checks if the move creates check
	Input- current player, other player, boars, tile destination
	Output- if the move creates check"""
	def canMoveMakeCheck(self, player, otherPlayer, board, originTile):
		#saves oribinal setting
		x = self._x
		y = self._y
		temp = originTile.getPiece()

		#gets source x and y
		self._x = originTile.getX()
		self._y = originTile.getY()

		#moves piece
		originTile.setPiece(self)

		#checks if there is check
		canEat = player.checkCheck(otherPlayer, board)

		#returns originale settings
		self._x = x
		self._y = y
		originTile.setPiece(temp)

		return canEat

	def checkMove(self, tile, board):
		pass

	def afterMove(self):
		pass