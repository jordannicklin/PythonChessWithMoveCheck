#include "Pipe.h"
#include <iostream>
#include <thread>

#include "Chess.h"

import Chess
import Visualizer

def main():

	chess = Chess.Chess()
	visualizer = Visualizer.Visualizer()

	#creates the board starting message
	currentBoard = "rnbkqbnrpppppppp################################PPPPPPPPRNBKQBNR1"

	#prints board
	#chess.printBoard()

	msgFromGraphics = ""

	while (msgFromGraphics != "quit"):
		# return result to graphics		
		(msgFromGraphics, preCheckBoard) = visualizer.getMove(currentBoard)
		#chess.printBoard()
		
		checkMsg = chess.processMove(msgFromGraphics)

		print(checkMsg)
		if checkMsg == "0" or checkMsg == "1":
			currentBoard = preCheckBoard

	#visualizer.drawBoard(msgToGraphics)
	pass
	cat = 0
	exit()

main()