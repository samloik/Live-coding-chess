import enum

class Color(enum.Enum):
    WHITE, BLACK = 1, 2

    def opposite(self):
        return Color.BLACK if self == Color.WHITE else Color.WHITE



if __name__ == '__main__':
    c = Color.WHITE
    b = Color.BLACK
    print(c)
    print(c.opposite())

    print(b)
    print(b.opposite())
