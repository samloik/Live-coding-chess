from Color import Color
from Coordinates import Coordinates
from Piece.Piece import Piece
from Board_.Board import AbstractBoard
from Board_.BoardUtils import BoardUtils

class LongRangePiece(Piece):
    def __init__(self, color: Color, coordinates: Coordinates):
        super().__init__(color, coordinates)

    def isSquareAvailableForMove(self, coordinates: Coordinates, board: AbstractBoard):
        result = super().isSquareAvailableForMove(coordinates, board)

        if result:
            # 1. get squares between current pos and target pos
            # 2. check that square is empty
            return self.isSquareAvailableForAtack(coordinates, board)

        return result


    def isSquareAvailableForAtack(self, coordinates: Coordinates, board: AbstractBoard):
        bu = BoardUtils()
        if self.coordinates.file == coordinates.file:
            coordList = bu.getVerticalCoordinatesBetween(self.coordinates, coordinates)
        elif self.coordinates.rank == coordinates.rank:
            coordList = bu.getHorizontalCoordinatesBetween(self.coordinates, coordinates)
        else:
            coordList = bu.getDiagonalCoordinatesBetween(self.coordinates, coordinates)

        for c in coordList:
            if not board.isSquareEmpty(c):
                return False

        return True