from Grid import Grid
from Blocks import *
import Parameters
import random
 
class GAAgent:
    def __init__( self, blockList = [], moves = [] ):
        if len( moves ) == 0:
            self.moves = self.getRandomMoves()
        else:
            self.moves = moves
 
        self.moveCounter = 0
 
        self.grid = Grid()
 
        self.blocksPlaced = 0
        self.gameOver = False
        self.fitnessScore = 0
        self.score = 0
        self.rowsCleared = 0
        self.rowHeight = 0
 
        self.blockList = blockList
        self.currentBlockNumber = 2
       
        if self.blockList[ 0 ] == "IBlock":
            self.currentBlock = IBlock()
        elif self.blockList[ 0 ] == "JBlock":
            self.currentBlock = JBlock()
        elif self.blockList[ 0 ] == "LBlock":
            self.currentBlock = LBlock()
        elif self.blockList[ 0 ] == "OBlock":
            self.currentBlock = OBlock()
        elif self.blockList[ 0 ] == "SBlock":
            self.currentBlock = SBlock()
        elif self.blockList[ 0 ] == "TBlock":
            self.currentBlock = TBlock()
        elif self.blockList[ 0 ] == "ZBlock":
            self.currentBlock = ZBlock()
 
        if self.blockList[ 1 ] == "IBlock":
            self.nextBlock = IBlock()
        elif self.blockList[ 1 ] == "JBlock":
            self.nextBlock = JBlock()
        elif self.blockList[ 1 ] == "LBlock":
            self.nextBlock = LBlock()
        elif self.blockList[ 1 ] == "OBlock":
            self.nextBlock = OBlock()
        elif self.blockList[ 1 ] == "SBlock":
            self.nextBlock = SBlock()
        elif self.blockList[ 1 ] == "TBlock":
            self.nextBlock = TBlock()
        elif self.blockList[ 1 ] == "ZBlock":
            self.nextBlock = ZBlock()
 
    def getRandomMoves( self ):
        initialMoves = []
        for i in range( Parameters.numMoves ):
            initialMoves.append( random.choice( Parameters.moves ) )
 
        return initialMoves
   
    def getRowHeight( self ):
        for i in range( self.grid.numRows ):
            for j in range( self.grid.numCols ):
                if self.grid.grid[ i ][ j ] > 0:
                    return 20 - i
        return 0
               
 
    def getNextMove( self ):
        move = self.moves[ self.moveCounter ]
        self.moveCounter += 1
        return move
   
    def getNextBlock( self ):
        self.currentBlock = self.nextBlock
        if self.blockList[ self.currentBlockNumber ] == "IBlock":
            self.nextBlock = IBlock()
        elif self.blockList[ self.currentBlockNumber ] == "JBlock":
            self.nextBlock = JBlock()
        elif self.blockList[ self.currentBlockNumber ] == "LBlock":
            self.nextBlock = LBlock()
        elif self.blockList[ self.currentBlockNumber ] == "OBlock":
            self.nextBlock = OBlock()
        elif self.blockList[ self.currentBlockNumber ] == "SBlock":
            self.nextBlock = SBlock()
        elif self.blockList[ self.currentBlockNumber ] == "TBlock":
            self.nextBlock = TBlock()
        elif self.blockList[ self.currentBlockNumber ] == "ZBlock":
            self.nextBlock = ZBlock()
        self.currentBlockNumber += 1
   
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
        self.getNextBlock()
        rowsCleared = self.grid.clearFullRows()
        self.updateScore( rowsCleared, 0 )
        self.rowsCleared += rowsCleared
        self.blocksPlaced += 1
        self.fitnessScore = self.fitnessScore + 1 + 10 * rowsCleared
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
 
    def updateScore( self, linesCleared, moveDownPoints ):
        if linesCleared == 1:
            self.score += 100
        if linesCleared == 2:
            self.score += 300
        if linesCleared == 3:
            self.score += 500
        self.score += moveDownPoints