from GameStateChecker import GameStateChecker
from Board_.BoardFactory import BoardFactory
from Board_.Move import Move
from Color import Color
from Board_.Board import Board
from Piece.King import King
from GameState import GameState

class CheckmateGameStateChecker(GameStateChecker):

    def check(self, board: Board, color: Color):
        # check if King under check
        # check that is no move to prevent this check

        # допущение, что король есть на доске
        king = [piece for piece in board.getPiecesByColor(color) if isinstance(piece, King)][0]

        if not board.isSquareAttackedByColor(king.coordinates, color.opposite()):
            return GameState.ONGOING

        pieces = board.getPiecesByColor(color)

        for piece in pieces:
            availableMoveSquares = piece.getAvailableMoveSquares(board)

            for coordinates in availableMoveSquares:
                clone = BoardFactory().copy(board)
                clone.makeMove(Move(piece.coordinates, coordinates))

                clonedKing = [piece for piece in clone.getPiecesByColor(color) if isinstance(piece, King)][0]

                clone.isSquareAttackedByColor(clonedKing.coordinates, color.opposite())

                if not clone.isSquareAttackedByColor(clonedKing.coordinates, color.opposite()):
                    return GameState.ONGOING

        if color == Color.WHITE:
            return GameState.CHECKMATE_TO_WHITE_KING
        else:
            return GameState.CHECKMATE_TO_BLACK_KING

