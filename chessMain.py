"""
This will be our main driver file. This will be responsible for handling user input and displaying the current game state object.
"""

import pygame as p
import chessEngine
WIDTH = HEIGHT = 512 #400 is aanother great choice
DIMENSION = 8    #Dimension of a square board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #For animation later
IMAGES = {}

"""
Initialize a dictionary of images. This will be called exactly once in the main
"""

def loadImages():
    pieces = ["wp","wR","wN","wB","wQ","wK","wB","wN","wR","bp","bR","bN","bB","bQ","bK","bB","bN","bR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))

# We can access an image by saying IMAGES["wp"]

"""
The main driver for our code. This will handle user input and update the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    loadImages() #only do  this once, before the while loop
    running = True
    sqSelected = () #initially no square is selected. Keep track of the last click of the user (tuple: (row,col))
    playerClicks = [] #keep track of player clicks. (Two tuples : [(6,4),(4,4)])

    while (running):
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (col,row): #The user clicked the same square twice
                    sqSelected = ()     #deselect
                    playerClicks = []   #clear player clicks
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)  # append for both 1st and 2nd click
                if len(playerClicks) == 2: #execcute this after 2nd click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () #reset user clicks
                    playerClicks = [] 


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)  #draw squares on the board
    #add in piece highlighting or move suggestion later 
    drawPieces(screen, gs.board)  #draw pieces on top of those squares  

"""
Draw squares on the board. The top left square is always light
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for c in range(DIMENSION): #will generate 0 to 7 numbers and iterate through them
        for r in range(DIMENSION):
            color = colors[((c+r)%2)]  #in a chess board, the row number + column number of a square indicates the color of the square.
                                     #white for even (0) and grey for odd(1)
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""
Draw pieces on the squares of the board using the current GameState's board variable 
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if(piece != "--"): #not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
