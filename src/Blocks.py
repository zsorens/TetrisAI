from Block import Block
from Position import Position

#the following code will all be described up top here since every class behaves the same with slight differences.
#below we have defined all the different types of blocks in tetris. There are seven possible blocks which could appear on the screen.
#We pass the file block which we have already created in another file to each of these block definitions.
#after passing our parameters and initializing the function we create cells which will make up the shape of these blocks.
#the values on the right are the possible roations of our block. For each rotation we pass a postion which will define the way
#the blocks are oriented based on how they are rotated. We use our position file to help define these positions also to make this process easier.


class LBlock( Block ):
    def __init__( self ):
        super().__init__( 1 )
        self.cells = {
            0: [ Position( 0, 2 ), Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ) ],
            1: [ Position( 0, 1 ), Position( 1, 1 ), Position( 2, 1 ), Position( 2, 2 ) ],
            2: [ Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 0 ) ],
            3: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 1 ), Position( 2, 1 ) ]
        }
        self.move( 0, 3 )

class JBlock( Block ):
    def __init__( self ):
        super().__init__( 2 )
        self.cells = {
            0: [ Position( 0, 0 ), Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ) ],
            1: [ Position( 0, 1 ), Position( 0, 2 ), Position( 1, 1 ), Position( 2, 1 ) ],
            2: [ Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 2 ) ],
            3: [ Position( 0, 1 ), Position( 1, 1 ), Position( 2, 0 ), Position( 2, 1 ) ]
        }
        self.move( 0, 3 )

class IBlock( Block ):
    def __init__( self ):
        super().__init__( 3 )
        self.cells = {
            0: [ Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ), Position( 1, 3 ) ],
            1: [ Position( 0, 2 ), Position( 1, 2 ), Position( 2, 2 ), Position( 3, 2 ) ],
            2: [ Position( 2, 0 ), Position( 2, 1 ), Position( 2, 2 ), Position( 2, 3 ) ],
            3: [ Position( 0, 1 ), Position( 1, 1 ), Position( 2, 1 ), Position( 3, 1 ) ]
        }
        self.move( -1, 3 )

class OBlock( Block ):
    def __init__( self ):
        super().__init__( 4 )
        self.cells = {
            0: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ) ],
            1: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ) ],
            2: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ) ],
            3: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ) ]
        }
        self.move( 0, 4 )

class SBlock( Block ):
    def __init__( self ):
        super().__init__( 5 )
        self.cells = {
            0: [ Position( 0, 1 ), Position( 0, 2 ), Position( 1, 0 ), Position( 1, 1 ) ],
            1: [ Position( 0, 1 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 2 ) ],
            2: [ Position( 1, 1 ), Position( 1, 2 ), Position( 2, 0 ), Position( 2, 1 ) ],
            3: [ Position( 0, 0 ), Position( 1, 0 ), Position( 1, 1 ), Position( 2, 1 ) ]
        }
        self.move( 0, 3 )

class TBlock( Block ):
    def __init__( self ):
        super().__init__( 6 )
        self.cells = {
            0: [ Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ) ],
            1: [ Position( 0, 1 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 1 ) ],
            2: [ Position( 1, 0 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 1 ) ],
            3: [ Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ), Position( 2, 1 ) ]
        }
        self.move( 0, 3 )

class ZBlock( Block ):
    def __init__( self ):
        super().__init__( 7 )
        self.cells = {
            0: [ Position( 0, 0 ), Position( 0, 1 ), Position( 1, 1 ), Position( 1, 2 ) ],
            1: [ Position( 0, 2 ), Position( 1, 1 ), Position( 1, 2 ), Position( 2, 1 ) ],
            2: [ Position( 1, 0 ), Position( 1, 1 ), Position( 2, 1 ), Position( 2, 2 ) ],
            3: [ Position( 0, 1 ), Position( 1, 0 ), Position( 1, 1 ), Position( 2, 0 ) ]
        }
        self.move( 0, 3 )