from Color import Color
from Coordinates import Coordinates
from Piece.Piece import Piece
from CoordinatesShift import CoordinatesShift
from Board_.Board import AbstractBoard

class King(Piece):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = []
        for fileShift in range(-1,2):
            for rankShift in range(-1,2):
                if fileShift == 0 and rankShift == 0:
                    continue
                moves.append(CoordinatesShift(fileShift, rankShift))
        return moves

    def isSquareAvailableForMove(self, coordinates: Coordinates, board: AbstractBoard):
        result = super().isSquareAvailableForMove(coordinates, board)

        if result:
            return not board.isSquareAttackedByColor(coordinates, self.color.opposite())
        else:
            return False