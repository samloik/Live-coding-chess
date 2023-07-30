from Coordinates import Coordinates

class Move:
    from_: Coordinates
    to: Coordinates

    def __init__(self, from_: Coordinates, to: Coordinates):
        self. from_ = from_
        self.to = to

    def __str__(self):
        return "<" + str(self.from_) + " to " + str(self.to) + ">"


if __name__ == '__main__':
    from File import File
    move = Move(Coordinates(File.A,1), Coordinates(File.C,3))
    print(move)