# https://www.youtube.com/watch?v=Pzydm8GZzMs&t=3s

from File import File
from Coordinates import Coordinates
from Board_.BoardFactory import BoardFactory
from Board_.BoardUtils import BoardUtils
from Game import Game


def main():
    for fileShift in range(-1, 2):
        print(fileShift)

def main3():
    b = BoardFactory()
    board = b.fromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    # board = b.fromFEN("3k4/8/5n2/2N5/3B4/8/8/3K4 w - - 0 1")
    # board = b.fromFEN("3k4/8/p7/8/R7/3K4/8/3K4 w - - 0 1")
    # board = b.fromFEN("3k4/8/p5n1/5B2/R7/3P4/P7/3K4 w - - 0 1")
    # board = b.fromFEN("3k4/6r1/8/1P2Q3/8/6P1/4r3/3K4 w - - 0 1")
    # board = b.fromFEN("3k4/6r1/8/1P2Q3/2B5/6P1/2R1r3/3K4 w - - 0 1")
    # board = b.fromFEN("1k6/6r1/5p2/4N3/2n3b1/3P2P1/2P5/6K1 w - - 0 1")
    # board = b.fromFEN("1k6/6r1/5p2/4N3/2n1B1b1/3P2P1/2P5/6K1 w - - 0 1")
    # board = b.fromFEN("8/8/4p3/8/4K3/8/4k3/8 w - - 0 1")
    # board = b.fromFEN("k7/8/4n3/8/4K3/8/8/8 w - - 0 1")
    # board = b.fromFEN("k7/8/1b6/8/4K3/8/8/8 w - - 0 1")
    # board = b.fromFEN("k7/8/1b6/2R5/4K3/8/8/8 w - - 0 1")
    # board = b.fromFEN("k4r2/8/8/r7/4KN2/2q1N3/8/8 w - - 0 1")
    # board = b.fromFEN("k7/8/4p3/8/4K3/8/8/8 w - - 0 1")
    # board = b.fromFEN("3k4/8/8/b7/8/8/2PK4/6N1 w - - 0 1")
    # board = b.fromFEN("8/8/8/8/6p1/3k1pP1/3p1P2/3K3N w - - 0 1")
    # board = b.fromFEN("4k3/4P3/8/4K3/8/8/8/8 w - - 0 1")
    # board = b.fromFEN("k2r4/8/8/8/2P1P3/2PKP3/2PPP3/8 w - - 0 1")
    # board = b.fromFEN("k2R4/8/8/8/2P1P3/2PKP3/2PPP3/8 w - - 0 1")

    # BoardConsoleRenderer().render(board)
    game = Game(board)

    game.gameLoop()

def main4():
    # b = BoardFactory()
    # board = b.fromFEN("3k4/8/5n2/2N5/3B4/8/8/3K4 w - - 0 1")
    # b = BoardFactory()
    # board = b.fromFEN("3k4/8/p7/8/R7/3K4/8/3K4 w - - 0 1")
    bu = BoardUtils()
    moves = bu.getGorizontalCoordinatesBetween(Coordinates(File.D, 4), Coordinates(File.H, 4))
    print(moves)

if __name__ == '__main__':
    # for i in range(-7, 8):
    #     if i == 0:
    #         continue
    #     print(i)
    main3()