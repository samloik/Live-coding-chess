from Color import Color
from Coordinates import Coordinates
from CoordinatesShift import CoordinatesShift
from Piece.Piece import Piece
from Piece.LongRangePiece import LongRangePiece

class Bishop(LongRangePiece):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = []
        # bottom-left to top-right
        for i in range(-7, 8):
            if i == 0:
                continue
            moves.append(CoordinatesShift(i,i))


        # top-left to bottom-right
        for i in range(-7, 8):
            if i == 0:
                continue
            moves.append(CoordinatesShift(i,-i))
        return moves






