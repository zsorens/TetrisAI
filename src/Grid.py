import pygame
import Colors

#we initialize our class Grid up top here
class Grid:
    def __init__(self): #start initializing here and set base values to our rows columns cell size ond the color.
        #this is used to initialize the look of our game or the grid.
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30
        self.grid = [ [ 0 for j in range( self.numCols ) ] for i in range( self.numRows ) ]
        self.colors = Colors.Colors.getCellColors()
#in this next function we draw the grid and initialize all of our values so we will have our game grid.
    def drawGrid( self, screen ):
        for row in range( self.numRows ):
            for col in range( self.numCols ):
                cellValue = self.grid[ row ][ col ]
                cellRect = pygame.Rect( 45 + col * self.cellSize + 1, 45 + row * self.cellSize + 1, self.cellSize - 1, self.cellSize - 1 )
                pygame.draw.rect( screen, self.colors[ cellValue ], cellRect )
#the next function will check if the rows or columns are within our grid.
    def isInside( self, row, col ):
        if row >= 0 and row < self.numRows and col >= 0 and col < self.numCols:
            return True
        return False
#the next function will test if the grid is empty based off of the columns and rows.
    def isEmpty( self, row, col ):
        if self.grid[ row ][ col ] == 0:
            return True
        return False
#here we check to see if one of our rows is filled up or not.
    def isRowFull( self, row ):
        for col in range( self.numCols ):
            if self.grid[ row ][ col ] == 0:
                return False
        return True
#here we create a function which will clear our row and set the values back to zero. 
    def clearRow( self, row ):
        for col in range( self.numCols ):
            self.grid[ row ][ col ] = 0
#in this function we will take a row and move it down. This will happen when a row is cleared and every row above needs to be shifted down.     
    def moveRowDown( self, row, numRows ):
        for col in range( self.numCols ):
            self.grid[ row + numRows ][ col ] = self.grid[ row ][ col ]
            self.grid[ row ][ col ] = 0
#iterates from the rows, from bottom to top and clears rows and moves them down as needed.
    def clearFullRows( self ):
        fullRows = 0
        for row in range( self.numRows - 1, 0 , -1 ):
            if self.isRowFull( row ):
                self.clearRow( row )
                fullRows += 1
            elif fullRows > 0:
                self.moveRowDown( row, fullRows )
        return fullRows
#defines a new game and sets the grid to zero resetting the game.
    def newGame( self ):
        for row in range( self.numRows ):
            for col in range( self.numCols ):
                self.grid[ row ][ col ] = 0