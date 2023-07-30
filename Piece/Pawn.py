from Color import Color
from Coordinates import Coordinates
from Piece.Piece import Piece
from CoordinatesShift import CoordinatesShift
from Board_.Board import AbstractBoard
from Board_.BoardUtils import BoardUtils

class Pawn(Piece):

    def __init__(self, color:Color, coordinates:Coordinates):
        super().__init__(color, coordinates)

    def getPieceMoves(self):
        moves = []

        if self.color == Color.WHITE:
            moves.append(CoordinatesShift(fileShift=0, rankShift=1))
            if self.coordinates.rank == 2:
                moves.append(CoordinatesShift(fileShift=0, rankShift=2))

            moves.append(CoordinatesShift(fileShift=-1, rankShift=1))
            moves.append(CoordinatesShift(fileShift=1, rankShift=1))
        else:
            moves.append(CoordinatesShift(fileShift=0, rankShift=-1))
            if self.coordinates.rank == 7:
                moves.append(CoordinatesShift(fileShift=0, rankShift=-2))
            moves.append(CoordinatesShift(fileShift=-1, rankShift=-1))
            moves.append(CoordinatesShift(fileShift=1, rankShift=-1))

        return moves

    def getPieceAtacks(self):
        movesToAtack = []

        if self.color == Color.WHITE:
            movesToAtack.append(CoordinatesShift(-1,1))
            movesToAtack.append(CoordinatesShift(1,1))
        else:
            movesToAtack.append(CoordinatesShift(-1,-1))
            movesToAtack.append(CoordinatesShift(1,-1))

        return movesToAtack

    def isSquareAvailableForMove(self, coordinates: Coordinates, board: AbstractBoard):
        if self.coordinates.file == coordinates.file:
            rankShift = abs(self.coordinates.rank - coordinates.rank)
            if rankShift == 2:
                coordBetween = BoardUtils.getVerticalCoordinatesBetween(self, self.coordinates, coordinates)
                return board.isSquareEmpty(coordBetween[0]) and board.isSquareEmpty(coordinates)
            return board.isSquareEmpty(coordinates)
        elif board.isSquareEmpty(coordinates):
            return False
        else:
            return board.getPiece(coordinates).color != self.color

