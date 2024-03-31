import TetrisGUI

# tetris driver
if __name__ == "__main__": #check to make sure our python script is being run in main
    TetrisGUI.initialize() #initialize our gui if true.

    while True: #create a infinite loop here so the code will run indefinitely.
        TetrisGUI.handleEvents() #this will handle user inputs in our program.
        TetrisGUI.drawScreen() #this is going to draw our game screen.
