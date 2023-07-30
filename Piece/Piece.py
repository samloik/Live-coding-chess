from Color import Color
from Coordinates import Coordinates
from Board_.AbstractBoard_ import AbstractBoard


class Piece:
    color: Color
    coordinates: Coordinates

    def __init__(self, color:Color, coordinates:Coordinates):
        self.color = color
        self.coordinates = coordinates

    def getAvailableMoveSquares(self, board: AbstractBoard):
        # return Coordinates
        result = []

        piecesMoves = self.getPieceMoves()
        for moves in piecesMoves:
            if self.coordinates.canShift(moves):
                newCoordinates = self.coordinates.shift(moves)

                if self.isSquareAvailableForMove(newCoordinates, board):
                    result.append(newCoordinates)

        return result

    def isSquareAvailableForMove(self, coordinates: Coordinates, board: AbstractBoard):
        return board.isSquareEmpty(coordinates) or board.getPiece(coordinates).color != self.color

    def getPieceMoves(self):
        # return CoodinatesShift
        return []

    def getPieceAtacks(self):
        # return CoodinatesShift
        return self.getPieceMoves()

    def getAtackedSquares(self, board: AbstractBoard):
        # return Coodinates
        pieceAtacks = self.getPieceAtacks()
        result = []

        for pieceAtack in pieceAtacks:
            if self.coordinates.canShift(pieceAtack):
                shiftedCoordinates = self.coordinates.shift(pieceAtack)

                if self.isSquareAvailableForAtack(shiftedCoordinates, board):
                    result.append(shiftedCoordinates)

        return result

    def isSquareAvailableForAtack(self, coordinates: Coordinates, board: AbstractBoard):
        return True