from Color import Color
from Board_ import Board
from BoardConsoleRenderer import BoardConsoleRenderer
from InputCoordinates import InputCoordinates
from GameState import GameState
from StalemateGameChecker import StalemateGameChecker
from CheckmateGameStateChecker import CheckmateGameStateChecker

class Game:
    board: Board
    renderer: BoardConsoleRenderer
    inputCoordinates: InputCoordinates
    checkers: list

    def __init__(self, board:Board):
        self.board = board
        self.renderer = BoardConsoleRenderer()
        self.inputCoordinates = InputCoordinates()
        self.checkers = [
            StalemateGameChecker(),
            CheckmateGameStateChecker()
        ]



    def gameLoop(self):
        colorToMove = Color.WHITE

        state = self.determineGameState(self.board, colorToMove)

        while state == GameState.ONGOING:
            # render
            self.renderer.render(self.board)
            print(f'{colorToMove.name} to move')

            # input

            move = self.inputCoordinates.inputMove(colorToMove, self.board, self.renderer)

            print(move)
            # checkIfKinginCheckAfterMove(from, to)
            # print("Your king is under atack!")

            # make move
            self.board.makeMove(move)

            # pass move
            colorToMove = colorToMove.opposite()

            state = self.determineGameState(self.board, colorToMove)


        self.renderer.render(self.board)

        print(f"Game ended with state = {state.name}")


    def determineGameState(self, board: Board, color: Color):
        for checker in self.checkers:
            state = checker.check(board, color)

            if state != GameState.ONGOING:
                return state

        return GameState.ONGOING

if __name__ == '__main__':
    state = GameState.ONGOING
    print(state.name)