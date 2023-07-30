from Coordinates import Coordinates
from File import File
from PieceFactory import PieceFactory
from Board_.Board import Board

class BoardFactory:

    def __init__(self):
        self.pieceFactory = PieceFactory()

    def fromFEN(self, fen: str):
        board = Board(fen)

        parts = fen.split(' ')
        piecePositions = parts[0]

        fenRows = piecePositions.split('/')

        for i in range(1,9):
            # print(i)
            rank = 9 - i
            row = fenRows[i-1]

            fileIndex = 0
            for char in row:
                if char.isdigit():
                    fileIndex += int(char)
                else:
                    file = File(fileIndex+1)
                    coordinates = Coordinates(file, rank)

                    board.setPiece(
                        coordinates,
                        self.pieceFactory.fromFENChar(char, coordinates)
                    )
                    fileIndex += 1

        return board

    def copy(self, source: Board):
        clone = self.fromFEN(source.startingFen)

        for move in source.moves:
            clone.makeMove(move)

        return clone

