from Color import Color
from File import File
from CoordinatesShift import CoordinatesShift

class Coordinates:
    file: File
    rank: int

    def __init__(self, file: File, rank: int):
        self.file = file
        self.rank = rank


    def __eq__(self, object):
        if self == object:
            return True
        if object == None or not isinstance(object, Coordinates):
            return False
        if object.file != self.file:
            return False
        return object.rank == self.rank


    def __repr__(self):
        return "" + chr(ord('A') - 1 + self.file.value) + str(self.rank)


    def __str__(self):
        return "" + chr(ord('A') - 1 + self.file.value) + str(self.rank)


    def shift(self, shift: CoordinatesShift):
        return Coordinates(file=File(self.file.value + shift.fileShift), rank=self.rank + shift.rankShift)


    def canShift(self, shift: CoordinatesShift):
        f = self.file.value + shift.fileShift
        r = self.rank + shift.rankShift

        if f < 1 or f > 8:
            return False

        if r < 1 or r > 8:
            return False

        return True
