
class CoordinatesShift:
    fileShift: int
    rankShift: int

    def __init__(self, fileShift: int, rankShift: int):
        self.fileShift = fileShift
        self.rankShift = rankShift

    def __repr__(self):
        return "[" + str(self.fileShift) + ":" + str(self.rankShift) + "] "

    def __str__(self):
        return "[" + str(self.fileShift) + ":" + str(self.rankShift) + "] "

if __name__ == '__main__':
    print(CoordinatesShift(1, 1))
    print(CoordinatesShift(7, -4))