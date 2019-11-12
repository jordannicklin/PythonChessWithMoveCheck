#pragma once

#include <iostream>
#include <stdio.h>
#include <ctype.h>

#include "Chess.h"
#include "Rook.h"
#include "Knight.h"
#include "Bishop.h"
#include "King.h"
#include "Queen.h"
#include "Pawn.h"

ZERO_ASCII = 48
A_ASCII = 97
BOARD_SIZE = 8


ROOK_TILE = 'R'
KNIGHT_TILE = 'N'
BISHOP_TILE = 'B'
KING_TILE = 'K'
QUEEN_TILE = 'Q'
PAWN_TILE = 'P'
EMPTY_TILE = '#'

from enum import Enum

import Board
import Player

import Rook
import Knight
import Bishop
import King
import Queen
import Pawn

class int_message(Enum): 
	LEGAL_MOVE = 1
	LEGAL_MOVE_CREATE_CHECK = 2
	NO_PIECE_IN_SOURCE = 3
	PIECE_IN_DES = 4
	CHECK_AFTER_MOVE = 5
	ILLEGAL_INDEX = 6
	INCORRECT_MOVEMENT = 7
	SRC_TILE_IS_DST_TILE = 8

class Chess:

	""" The function creates the dynamic variabels
	Input- none
	Output- none """
	def __init__(self):
		self._whiteTurn = False
		startMessage = "rnbkqbnrpppppppp################################PPPPPPPPRNBKQBNR"
		temp = 0 # Piece*

		#creates variabels
		self._board = Board.Board()
		self._playerWhite = Player.Player()
		self._playerBlack = Player.Player()

		i = 0
		while (i < len(startMessage)):
			#print(i % BOARD_SIZE)
			#calculates x and y using i
			x = (i % BOARD_SIZE)# + A_ASCII
			y = int((i / BOARD_SIZE))# + ZERO_ASCII

			#checks piece in place of i and creates piece matching type
			case = startMessage[i].upper()
			#print(case)

			if case == 'R':
				temp = Rook.Rook(x, y, startMessage[i])
			elif case == 'N':
				temp = Knight.Knight(x, y, startMessage[i])
			elif case == 'B':
				temp = Bishop.Bishop(x, y, startMessage[i])
			elif case == 'K':
				temp = King.King(x, y, startMessage[i])
			elif case == 'Q':
				temp = Queen.Queen(x, y, startMessage[i])
			elif case == 'P':
				temp = Pawn.Pawn(x, y, startMessage[i])
			elif case == '#':
				temp = 0

			#checks if created new piece
			if (temp):
				#checks if the piece is white
				if (startMessage[i].upper() == startMessage[i]):
					#inserts the piece to the white player
					self._playerWhite.insertPiece(temp)
				else:
					#inserts the piece to the black player
					self._playerBlack.insertPiece(temp)

				#inserts the piece to the matching tile in board
				#print(self._board.getTile(x, y))
				self._board.getTile(x, y).setPiece(temp)

			i = i + 1

	""" The function delets all of the dynamic variabels
	Input- none
	Output- none 
	Chess::~Chess()
	{
		delete _board
		delete _playerWhite
		delete _playerBlack
	}"""

	#string
	""" The function checks a move and returns matching message
	Input- frontend string of the move
	Output- message """
	def processMove(self, move):
		#checks if the movemennt string has 4 indexes
		if (len(move) != 4):
			return "5"
		
		#seperates input fom frontend to x source, y source, x destination, ydestination
		xSrc = move[0] 
		ySrc = move[1] #'0' + (BOARD_SIZE - (move[1] - '0'))
		xDst = move[2]
		yDst = move[3] #'0' + (BOARD_SIZE - (move[3] - '0'))

		#checks if the piece did ot move
		if (xSrc == xDst and ySrc == yDst):
			return "7"

		#gets the pieces at source tile and destination tile
		srcPiece = self._board.getTile(xSrc, ySrc).getPiece() #Piece* 
		dstPiece = self._board.getTile(xDst, yDst).getPiece()

		#checks if the source tile has a piece of the current player
		if ( not srcPiece or srcPiece.isWhite() != self._whiteTurn):
			return "2"

		#checks if the destination tile has a piece of the current player
		if (dstPiece and dstPiece.isWhite() == self._whiteTurn):
			return "3"

		ans = str(srcPiece.checkDistanation(xDst, yDst, self._board))

		if (ans == "0"):
			#gets current player and opposite player based on current turn
			if (self._whiteTurn):
				curPlayer = self._playerWhite
				oppositePlayer = self._playerBlack
			else:
				curPlayer = self._playerBlack
				oppositePlayer = self._playerWhite
			
			#checks if the move made check on other player
			if (srcPiece.canMoveMakeCheck(oppositePlayer, curPlayer, self._board, self._board.getTile(xDst, yDst))):
				ans = "1"

			#checks if current player has check after move
			if (srcPiece.canMoveMakeCheck(curPlayer, oppositePlayer, self._board, self._board.getTile(xDst, yDst))):
				ans = "4"

		#if there is no error then countinues with the game
		if (ans == "0" or ans == "1"):
			#moves the piece on source tile
			srcPiece.move(self._board.getTile(xDst, yDst), self._board)

			#moves to next turn
			self._whiteTurn = not self._whiteTurn
		
		#returns message
		return ans

	""" The function prints the board
	Input- none
	Output- none """
	def printBoard(self):
		pieceType = ''

		i = 0
		while (i < BOARD_SIZE):
			j = 0
			while (j < BOARD_SIZE):
				#sets the type to default
				pieceType = '#'

				#checks if there is a piece in the tile in the place of x and y
				#print(self._board.getTile(j, i).getPiece())
				if (self._board.getTile(j, i).getPiece()):#(A_ASCII + j, ZERO_ASCII + i).getPiece()):
					#gets the type of the tile
					pieceType = self._board.getTile(j, i).getPiece().getType()#(A_ASCII + j, ZERO_ASCII + i).getPiece().getType()

				#prints the type
				print(pieceType + " ", end =" ")
				j = j + 1

			#prints /n
			print('')

			i = i + 1