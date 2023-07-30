from Color import Color
from Coordinates import Coordinates
from Board_.AbstractBoard_ import AbstractBoard
from Piece.Piece import Piece
from contains import contains
from Board_.Move import Move

class Board(AbstractBoard):
    # pieces = {}
    # moves = []


    def __init__(self, fen: str):
        self.pieces = {}
        self. moves = []
        self.startingFen = fen

        # TODO возможно нужно заполнить доску - проверить как у автора


    def setPiece(self, coordinates: Coordinates, piece: Piece):
        self.pieces[str(coordinates)] = piece
        piece.coordinates = coordinates

    def removePiece(self, coordinates: Coordinates):
        del self.pieces[str(coordinates)]

    def makeMove(self, move: Move):
        piece = self.getPiece(move.from_)
        self.removePiece(move.from_)
        self.setPiece(move.to, piece)

        self.moves.append(move)


    def isSquareEmpty(self, coordinates: Coordinates):
        return not str(coordinates) in self.pieces.keys()

    def getPiece(self, coordinates:Coordinates):
        return self.pieces[str(coordinates)]

    def setupDefaultPosition(self):
        # set pawns
        for file in File:
            self.setPiece(Coordinates(file, 2), Pawn(Color.WHITE, Coordinates(file, 2)))
            self.setPiece(Coordinates(file, 7), Pawn(Color.BLACK, Coordinates(file, 7)))

        # set Rook
        self.setPiece(Coordinates(file.A, 1), Rook(Color.WHITE, Coordinates(file.A, 1)))
        self.setPiece(Coordinates(file.H, 1), Rook(Color.WHITE, Coordinates(file.H, 1)))
        self.setPiece(Coordinates(file.A, 8), Rook(Color.BLACK, Coordinates(file.A, 8)))
        self.setPiece(Coordinates(file.H, 8), Rook(Color.BLACK, Coordinates(file.H, 8)))

        # set Knight
        self.setPiece(Coordinates(file.B, 1), Knight(Color.WHITE, Coordinates(file.B, 1)))
        self.setPiece(Coordinates(file.G, 1), Knight(Color.WHITE, Coordinates(file.G, 1)))
        self.setPiece(Coordinates(file.B, 8), Knight(Color.BLACK, Coordinates(file.B, 8)))
        self.setPiece(Coordinates(file.G, 8), Knight(Color.BLACK, Coordinates(file.G, 8)))

        # set Bishop
        self.setPiece(Coordinates(file.C, 1), Bishop(Color.WHITE, Coordinates(file.C, 1)))
        self.setPiece(Coordinates(file.F, 1), Bishop(Color.WHITE, Coordinates(file.F, 1)))
        self.setPiece(Coordinates(file.C, 8), Bishop(Color.BLACK, Coordinates(file.C, 8)))
        self.setPiece(Coordinates(file.F, 8), Bishop(Color.BLACK, Coordinates(file.F, 8)))

        # set Queens
        self.setPiece(Coordinates(file.D, 1), Queen(Color.WHITE, Coordinates(file.D, 1)))
        self.setPiece(Coordinates(file.D, 8), Queen(Color.BLACK, Coordinates(file.D, 8)))

        # set Kings
        self.setPiece(Coordinates(file.E, 1), King(Color.WHITE, Coordinates(file.E, 1)))
        self.setPiece(Coordinates(file.E, 8), King(Color.BLACK, Coordinates(file.E, 8)))


    def isSquareDark(self, coordinates: Coordinates):
        return (coordinates.file.value + coordinates.rank + 1) % 2


    def isSquareAttackedByColor(self, coordinates: Coordinates, color:Color):
        pieces = self.getPiecesByColor(color)

        for piece in pieces:
            atackedSquares = piece.getAtackedSquares(self)

            if contains(atackedSquares, coordinates):
                return True

        return False


    def getPiecesByColor(self, color: Color):
        coloredPieces = []
        for pieceKey in self.pieces.keys():
            if self.pieces[pieceKey].color == color:
                coloredPieces.append(self.pieces[pieceKey])
        return coloredPieces

    def __str__(self):
        # TODO отобразить доску
        line = "_str_: "
        for key in self.pieces.keys():
            line += "<"+ f"{'W' if self.pieces[key].color == Color.WHITE else 'B'}:{self.pieces[key].__class__.__name__}:{self.pieces[key].coordinates}" + "> "
        return line


if __name__ == '__main__':
    from Board_.BoardFactory import BoardFactory
    b = BoardFactory()
    board = b.fromFEN("3k4/8/8/b7/8/8/2PK4/6N1 w - - 0 1")
    print(board)



