from Grid import Grid
from Blocks import *
import random

class Game:
    def __init__( self ):
        self.grid = Grid()
        self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock() ]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()
        self.gameOver = False
        self.score = 0

    def getRandomBlock( self ):
        if len( self.blocks ) == 0:
            self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock() ]
        block = random.choice( self.blocks )
        self.blocks.remove( block )
        return block
    
    def draw( self, screen ):
        self.grid.drawGrid( screen )
        self.currentBlock.draw( screen, 45, 45 )

    def moveLeft( self ):
        self.currentBlock.move( 0, -1 )
        if self.blockInsideGrid() == False or self.blockFits() == False:
            self.currentBlock.move( 0, 1 )
    
    def moveRight( self ):
        self.currentBlock.move( 0, 1 )
        if self.blockInsideGrid() == False or self.blockFits() == False:
            self.currentBlock.move( 0, -1 )

    def moveDown( self ):
        self.currentBlock.move( 1, 0 )
        if self.blockInsideGrid() == False or self.blockFits() == False:
            self.currentBlock.move( -1, 0 )
            self.killBlock()
    
    def killBlock( self ):
        tiles = self.currentBlock.getCellPositions()
        for position in tiles:
            self.grid.grid[ position.row ][ position.col ] = self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
        rowsCleared = self.grid.clearFullRows()
        self.updateScore( rowsCleared, 0 )
        if self.blockFits() == False:
            self.gameOver = True

    def blockFits( self ):
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if self.grid.isEmpty( tile.row, tile.col ) == False:
                return False
        return True

    def rotate( self ):
        self.currentBlock.rotate()
        if self.blockInsideGrid() == False or self.blockFits() == False:
            self.currentBlock.undoRotate()

    def blockInsideGrid( self ):
        tiles = self.currentBlock.getCellPositions()
        for tile in tiles:
            if self.grid.isInside( tile.row, tile.col ) == False:
                return False
        return True
    
    def newGame( self ):
        self.score = 0
        self.grid.newGame()
        self.blocks = [ IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock() ]
        self.currentBlock = self.getRandomBlock()
        self.nextBlock = self.getRandomBlock()

    def updateScore( self, linesCleared, moveDownPoints ):
        if linesCleared == 1:
            self.score += 100
        if linesCleared == 2:
            self.score += 300
        if linesCleared == 3:
            self.score += 500
        self.score += moveDownPoints