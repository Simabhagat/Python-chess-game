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

    while (running):
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)  #draw squares on the board
    #add in piece highlighting or move suggestion later
    # drawPieces(screen, gs.board)  #draw pieces on top of those squares  

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
# def drawPieces(screen, board):

if __name__ == "__main__":
    main()
