from Color import Color
from File import File
from Coordinates import Coordinates
from Board_.AbstractBoard_ import AbstractBoard
from contains import contains
from BoardConsoleRenderer import BoardConsoleRenderer
from Board_.Move import Move
from Board_.BoardFactory import BoardFactory
from Piece.King import King

class InputCoordinates:

    def input(self):
        while True:
            print('Pleasse enter coordinates (ex. a1): ')
            # a1
            coord = input();

            if len(coord) != 2:
                print('Invalid format')
                continue

            if not coord[0].isalpha() and ():
                print('Invalid format')
                continue

            if not coord[1].isdigit():
                print('Invalid format')
                continue

            rank = int(coord[1])

            if not 1 <= rank <= 8:
                print('Invalid format')
                continue

            file = coord[0].upper()

            if not 'A' <= file <= 'H':
                print('Invalid format')
                continue

            return Coordinates(File[file], rank)

    def inputPieceCoordinatesForColor(self, color: Color, board: AbstractBoard):
        while True:
            print('Enter coordinates for a Piece to move')
            coordinates = self.input()

            if board.isSquareEmpty(coordinates):
                print('Empty square')
                continue

            piece = board.getPiece(coordinates)
            if piece.color != color:
                print('Wrong color')
                continue

            availableMovesSquares = piece.getAvailableMoveSquares(board)

            if len(availableMovesSquares) == 0:
                print('Blocked Piece')
                continue

            return coordinates

    def inputAvailableSquare(self, coordinatesList: list):
        while True:
            print('Enter your move for selected Piece')
            inputCoord = self.input()

            if not contains(coordinatesList, inputCoord):
                print('Non-available square')
                continue

            return inputCoord

    def inputMove(self, color: Color, board: AbstractBoard, renderer: BoardConsoleRenderer):
        while True:
            sourceCoordinates = self.inputPieceCoordinatesForColor(color, board)

            piece = board.getPiece(sourceCoordinates)
            availableMoveSquares = piece.getAvailableMoveSquares(board)

            renderer.render(board, piece)
            targetCoordinates = self.inputAvailableSquare(availableMoveSquares)

            move = Move(sourceCoordinates, targetCoordinates)
            print(f"Your move: {move}")

            if self.validateIfKinginCheckAfterMove(board, color, move):
                print("Your king is under atack!")
                continue

            return move

    def validateIfKinginCheckAfterMove(self, board:AbstractBoard, color:Color, move:Move):
        # Board_ copy
        bf = BoardFactory()
        copy = bf.copy(board)
        print(f'{copy is board=}')
        # copy.move(move)
        copy.makeMove(move)
        # king king=...
        pieces = copy.getPiecesByColor(color)
        # допущение, что король есть на доске
        king = [piece for piece in pieces if isinstance(piece, King)][0]
        return copy.isSquareAttackedByColor(king.coordinates, color.opposite())
        # king.coordinates under atack => false
        # return true

        # TODO найти почему делается ход на доске оригинале


