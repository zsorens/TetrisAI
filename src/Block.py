from Colors import Colors
from Position import Position
import pygame


#create the class block which will initialize all atributes of a tetrinome, pass two parameters which are self and id
class Block:
    def __init__( self, id ):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotation = 0
        self.rowOffset = 0
        self.colOffset = 0
        self.colors = Colors.getCellColors()

#create a draw function which is used to draw all the blocks onto the game screen.
    def draw( self, screen, xOffset, yOffset ):
        tiles = self.getCellPositions()
        for tile in tiles:
            tileRect = pygame.Rect( xOffset + tile.col * self.cellSize + 1, yOffset + tile.row * self.cellSize + 1, self.cellSize - 1, self.cellSize - 1 )
            pygame.draw.rect( screen, self.colors[ self.id ], tileRect )

#this will update our rows and columns allowing our blocks to move in the game.
    def move( self, rows, cols ):
        self.rowOffset += rows
        self.colOffset += cols

#we use the getCellPositions function to return the current position of the blocks cell. This is determined by offset, rotation and position.
    def getCellPositions( self ):
        tiles = self.cells[ self.rotation ]
        movedTiles = []
        for position in tiles:
            position = Position( position.row + self.rowOffset, position.col + self.colOffset )
            movedTiles.append( position )
        return movedTiles

#This function is used to rotate our block. Once it exceeds the possible number of trotations it is returned to it will wrap around
    def rotate( self ):
        self.rotation += 1
        if self.rotation == len( self.cells ):
            self.rotation = 0

#behaves the same way as rotate except will decrement the rotation and go negatively.When the number is negative it wraps to the maximum.
    def undoRotate( self ):
        self.rotation -= 1
        if self.rotation == -1:
            self.rotation = len( self.cells ) - 1
