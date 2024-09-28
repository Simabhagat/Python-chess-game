"""
This class will be responsible for storing all the information about the current state of a chess game. It will also be responsible for
determining the valid moves at the current state of the game. It will also keep a move log
"""
class GameState():
    #board is an 8x8 two dimensional list, each element of the list has two characters
    #The first character represents the color of the piece, "b" for black or "w" for white
    #The second character represents the type of the piece, "p" for pawn, "R" for rook, "N" for knight, "B" for bishop, "Q" for queen, "K" for king
    #"--" represents the empty square
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whiteToMove = True
        self.logMove = []