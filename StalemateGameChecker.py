from Color import Color
from Board_.Board import Board
from GameState import GameState
from GameStateChecker import GameStateChecker

class StalemateGameChecker(GameStateChecker):

    def check(self, board: Board, color: Color):
        pieces = board.getPiecesByColor(color)

        for piece in pieces:
            availableMoveSquares = piece.getAvailableMoveSquares(board)

            if len(availableMoveSquares) > 0:
                return GameState.ONGOING

        return GameState.STALEMATE