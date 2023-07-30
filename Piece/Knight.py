from Color import Color
from Coordinates import Coordinates
from Piece.Piece import Piece
from CoordinatesShift import CoordinatesShift

class Knight(Piece):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = [
            CoordinatesShift(1, 2),
            CoordinatesShift(2, 1),

            CoordinatesShift(2, -1),
            CoordinatesShift(1, -2),

            CoordinatesShift(-2, -1),
            CoordinatesShift(-1, -2),

            CoordinatesShift(-2, 1),
            CoordinatesShift(-1, 2)
        ]
        return moves
