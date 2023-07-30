from Color import Color
from File import File
from Coordinates import Coordinates
from Piece.Piece import Piece
from Board_.Board import Board
from contains import contains

class BoardConsoleRenderer():
    ANSI_RESET = "\033[0m"
    ANSI_WHITE_PIECE_COLOR = "97"
    ANSI_BLACK_PIECE_COLOR = "30"
    ANSI_WHITE_SQUARE_COLOR = "47"
    ANSI_BLACK_SQUARE_COLOR = "100"
    ANSI_HIGHLIGHT_SQUARE_COLOR = "45"

    def render(self, board: Board, pieceToMove: Piece = None):
        if pieceToMove == None:
            availableMoveSquares = []
        else:
            availableMoveSquares = pieceToMove.getAvailableMoveSquares(board)

        print('   A  B  C  D  E  F  G  H')
        for rank in range(8, 0, -1):
            line = str(rank) + ' '
            for file in File:
                coordinates = Coordinates(file, rank)

                isHighLight = contains(availableMoveSquares, coordinates)

                if board.isSquareEmpty(coordinates):
                    line += self.getStringForEmptySquare(coordinates, board, isHighLight)
                else:
                    line += self.getPieceSprite(board.getPiece(coordinates), board, isHighLight)
            line += self.ANSI_RESET
            line += ' ' + str(rank)
            print(line)
        print('   A  B  C  D  E  F  G  H')


    def colorizeSprite(self, sprite:str, pieceColor:Color, isSquareDark: bool, isHighLighted:bool):

        if pieceColor == Color.WHITE:
            PieceColor = self.ANSI_WHITE_PIECE_COLOR
        else:
            PieceColor = self.ANSI_BLACK_PIECE_COLOR

        if isHighLighted:
            SquareColor = self.ANSI_HIGHLIGHT_SQUARE_COLOR
        else:
            if isSquareDark:
                SquareColor = self.ANSI_BLACK_SQUARE_COLOR
            else:
                SquareColor = self.ANSI_WHITE_SQUARE_COLOR

        return '\033[0;' + PieceColor + ';' + SquareColor + 'm' + sprite



    def getStringForEmptySquare(self, coordinates: Coordinates, board:Board, isHighLighted:bool):
        return self.colorizeSprite("   ", Color.BLACK, board.isSquareDark(coordinates), isHighLighted)


    def selectUnicodeSpriteForPiece(self, piece: Piece):
        pieceName = {
            "Pawn": "p",
            "Knight": "k",
            "Bishop": "B",
            "Rook": "R",
            "Queen": "Q",
            "King": "K",
        } [piece.__class__.__name__]
        return pieceName


    def getPieceSprite(self, piece:Piece, board:Board, isHighLighted:bool):
        return self.colorizeSprite(
            " " + self.selectUnicodeSpriteForPiece(piece) + " ", piece.color,
            board.isSquareDark(piece.coordinates), isHighLighted
        )
