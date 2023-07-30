from Color import Color
from Coordinates import Coordinates
from Piece.Bishop import Bishop
from Piece.Rook import Rook

class Queen(Bishop, Rook):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = Bishop.getPieceMoves(self)
        moves.extend(Rook.getPieceMoves(self))

        return moves
