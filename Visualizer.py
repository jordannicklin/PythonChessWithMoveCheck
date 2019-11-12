
import pygame
import os

class Visualizer:

    def __init__(self):
        pygame.init()
        self._size = (800, 800)
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('Chess')
        self._font = pygame.font.SysFont('Arial', 100)

    def drawBoard(self, pieceMsg):
        self._screen.fill( (255,255,255) )
        pygame.display.update()

        """self._screen.blit(self.get_image('\img\KnightW.png'), (20, 20))
        knightWImg = pygame.image.load("\img\KnightW.png")
        knightBImg = pygame.image.load('img/KnightB.png')
        queenWImg = pygame.image.load('img/QueenW.png')
        queenBImg = pygame.image.load('img/QueenB.png')
        kingWImg = pygame.image.load('img/KingW.png')
        kingBImg = pygame.image.load('img/KingB.png')
        pawnWImg = pygame.image.load('img/PawnW.png')
        pawnBImg = pygame.image.load('img/PawnB.png')"""


        i = 0
        while (i < 790):
            j = 0
            while (j < 790):
                if i % 200:
                    if j % 200:
                        pygame.draw.rect(self._screen, (0 , 0 , 0), (i, j, 100, 100))
                    else:
                        pygame.draw.rect(self._screen, (255 , 255 , 255), (i, j, 100, 100))

                else:
                    if j % 200:
                        pygame.draw.rect(self._screen, (255 , 255 , 255), (i, j, 100, 100))
                    else:
                        pygame.draw.rect(self._screen, (0 , 0 , 0), (i, j, 100, 100))
                
                if pieceMsg[int(i / 100 + (j/100) * 8)] != '#':
                    self._screen.blit(self._font.render(pieceMsg[int(i / 100 + (j/100) * 8)], True, (100,100,100)), (i, j))
                pygame.display.update()
                j = j + 100

            i = i + 100
            pygame.display.update()

    def getMove(self, currentBoard):

        self.drawBoard(currentBoard)
        selectedPieceIndex = -1
        selectedPieceLocationIndex = -1

        returnmsg = ""

        running = True

        while running and selectedPieceLocationIndex == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return ("quit", "quit")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouse_x, mouse_y = event.pos
                        returnmsg = returnmsg + str(int(mouse_x / 100)) + str(int(mouse_y/100))
                        if selectedPieceIndex == -1:           
                            selectedPieceIndex = int(mouse_x / 100 + int(mouse_y/100) * 8)
                        else:
                            selectedPieceLocationIndex = int(mouse_x / 100 + int(mouse_y/100) * 8)
        
        piece = currentBoard[selectedPieceIndex]
        currentBoard = list(currentBoard)
        currentBoard[selectedPieceIndex] = "#"
        currentBoard[selectedPieceLocationIndex] = piece
        currentBoard = "".join(currentBoard)
        
        #print(currentBoard)
        self.drawBoard(currentBoard)
        pass
        return (returnmsg, currentBoard)

