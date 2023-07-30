from Color import Color
from Coordinates import Coordinates
from CoordinatesShift import CoordinatesShift
from Piece.LongRangePiece import LongRangePiece

class Rook(LongRangePiece):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = []
        # left to ight
        for i in range(-7, 8):
            if i == 0:
                continue
            moves.append(CoordinatesShift(i,0))


        # bottom to top
        for i in range(-7, 8):
            if i == 0:
                continue
            moves.append(CoordinatesShift(0,i))
        return moves



