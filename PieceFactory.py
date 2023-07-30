from Color import Color
from Coordinates import Coordinates

from Piece.Pawn import Pawn
from Piece.Bishop import Bishop
from Piece.Rook import Rook
from Piece.Knight import Knight
from Piece.Queen import Queen
from Piece.King import King

class PieceFactory():

    def fromFENChar(self, fenChar: str, coordinates: Coordinates):
        try:
            piece = {
                'p': Pawn(Color.BLACK, coordinates),
                'P': Pawn(Color.WHITE, coordinates),
                'r': Rook(Color.BLACK, coordinates),
                'R': Rook(Color.WHITE, coordinates),
                'n': Knight(Color.BLACK, coordinates),
                'N': Knight(Color.WHITE, coordinates),
                'b': Bishop(Color.BLACK, coordinates),
                'B': Bishop(Color.WHITE, coordinates),
                'q': Queen(Color.BLACK, coordinates),
                'Q': Queen(Color.WHITE, coordinates),
                'k': King(Color.BLACK, coordinates),
                'K': King(Color.WHITE, coordinates)
            } [fenChar]
            return piece
        except Exception as Err:
            print("Unknown FEN char!")
            raise RuntimeError