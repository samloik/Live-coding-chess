from Color import Color
from Coordinates import Coordinates
from Board_.Move import Move

class AbstractBoard:

    def __init__(self, fen: str):
        pass

    def makeMove(self, move: Move):
        pass

    def isSquareEmpty(self, coordinates: Coordinates):
        return true

    def getPiece(self, coordinates: Coordinates):
        return None

    def isSquareAttackedByColor(coordinates: Coordinates, color: Color):
        return True

    def __str__(self):
        return None