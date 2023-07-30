from File import File
from Coordinates import Coordinates


class BoardUtils:
    def getDiagonalCoordinatesBetween(self, source: Coordinates, target: Coordinates):
        # допущение - клетки лежат на одной диагонали
        result = []

        fileShift = 1 if source.file.value < target.file.value else -1
        rankShift = 1 if source.rank < target.rank else -1

        fileIndex = source.file.value + fileShift
        rankIndex = source.rank + rankShift
        while fileIndex != target.file.value and rankIndex != target.rank:
            result.append(Coordinates(File(fileIndex), rankIndex))

            fileIndex += fileShift
            rankIndex += rankShift

        return result

    def getVerticalCoordinatesBetween(self, source: Coordinates, target: Coordinates):
        # допущение - клетки лежат на одной вертикали
        result = []

        rankShift = 1 if source.rank < target.rank else -1

        rankIndex = source.rank + rankShift
        while rankIndex != target.rank:
            result.append(Coordinates(source.file, rankIndex))

            rankIndex += rankShift

        return result

    def getHorizontalCoordinatesBetween(self, source: Coordinates, target: Coordinates):
        # допущение - клетки лежат на одной горизонтали
        result = []

        fileShift = 1 if source.file.value < target.file.value else -1

        fileIndex = source.file.value + fileShift
        while fileIndex != target.file.value:
            result.append(Coordinates(File(fileIndex), source.rank))

            fileIndex += fileShift

        return result