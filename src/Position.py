#a class which is used for the positions. The way tetris is set up we just need our row and column for the positions.
class Position:
    def __init__( self, row, col ):
        self.row = row
        self.col = col