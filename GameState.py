import enum

class GameState(enum.Enum):
    ONGOING, STALEMATE, CHECKMATE_TO_WHITE_KING, CHECKMATE_TO_BLACK_KING = 1, 2, 3, 4
