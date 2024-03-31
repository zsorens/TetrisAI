import pygame
import sys
import Parameters
from Blocks import *
from Game import Game
from GAAgent import GAAgent
from TetrisGenAlg import TetrisGenAlg
from WOCGenAlg import WOCGenAlg

# Initialize constants for screen size, button size, and positioning
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Constants for button sizing
BUTTON_PADDING_SIZE = 20
FULL_SIZE_BUTTON_SIZE_Y = 40
FULL_SIZE_BUTTON_SIZE_X = ( SCREEN_WIDTH / 2 )
HALF_SIZE_BUTTON_SIZE_Y = 40
HALF_SIZE_BUTTON_SIZE_X = ( SCREEN_WIDTH / 4 ) - BUTTON_PADDING_SIZE / 2

SCREEN_PADDING = 30

# Initialize constants for colors
WHITE = ( 255, 255, 255 )
BLUE = ( 0, 100, 255 )
BLACK = ( 0, 0, 0 )
LIGHT_GRAY = ( 211, 211, 211 )
RED = ( 255, 0, 0 )

def initialize():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption( "Tetris" )

    # initialize the game
    global game
    game = Game()

    # initialize the tetris genetic algorithm
    global TetrisGA
    TetrisGA = TetrisGenAlg()

    # initialize the best agent
    global bestAgent
    bestAgent = TetrisGA.getBestAgent()

    # initialize the timer to control framerate
    global game_update
    game_update = pygame.USEREVENT
    pygame.time.set_timer( game_update, 200 )

    # initialize the clock
    global clock
    clock = pygame.time.Clock()

    # Initialize the screen for pygame
    global screen
    screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )

    # Initialize the font for buttons
    global BUTTON_FONT    
    BUTTON_FONT = pygame.font.Font( None, 24 )

    global SCORE_FONT
    SCORE_FONT = pygame.font.Font( None, 36 )

    drawScreen()
    
    # Update the screen with these changes
    pygame.display.update()

def drawScreen():
    # fill screen with black to erase everything
    screen.fill( BLACK )

    # draw the appropriate component depending on the running state
    if Parameters.runningState == 0:
        drawMenu()
    if Parameters.runningState == 1:
        drawGASettings()
    if Parameters.runningState == 2:
        drawTetris()
    if Parameters.runningState == 3:
        drawGATetris()
    if Parameters.runningState == 4:
        drawWOCTetris()

    # update the display
    pygame.display.update()

# draws the components of the menu
def drawMenu():
    drawPlayTetrisButton()
    drawRunGAButton()
    drawGASettingsButton()

# draws the components of the ga settings
def drawGASettings():
    drawPopulationSizeControls()
    drawMutationRateControls()
    drawWisdomOfCrowdsButton()
    drawWisdomOfCrowdsRateControls()
    drawSettingsBackButton()

# draws components of the ga settings
def drawTetris():
    drawScore( game.score )
    drawNextBlock( game.nextBlock )
    drawReplayButton()
    drawTetrisBackButton()
    game.draw( screen )

# draws the woc tetris components
def drawWOCTetris():
    drawScore(Parameters.best_agent.score)
    drawFitnessScore( Parameters.best_agent.fitnessScore )
    # drawRowsCleared( bestAgent.rowsCleared )
    # drawGenerationNumber( TetrisGA.generation )
    drawNextBlock( Parameters.best_agent.nextBlock )
    drawGABackButton()
    Parameters.best_agent.draw( screen )

# draws the components for the tetris genetic algorithm
def drawGATetris():
    drawScore( bestAgent.score )
    drawFitnessScore( bestAgent.fitnessScore )
    drawRowsCleared( bestAgent.rowsCleared )
    drawGenerationNumber( TetrisGA.generation )
    drawNextBlock( bestAgent.nextBlock )
    drawGABackButton()
    bestAgent.draw( screen )

# draws the button to play tetris for the menu
def drawPlayTetrisButton():
    global playTetrisButtonRect

    xPos = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPos = SCREEN_HEIGHT / 4 + SCREEN_PADDING + ( 0 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 0 * BUTTON_PADDING_SIZE )

    playTetrisButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    playTetrisButtonText = BUTTON_FONT.render( "Play Tetris", True, WHITE )
    playTetrisButtonTextRect = playTetrisButtonText.get_rect( center = ( ( xPos + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( playTetrisButtonText, playTetrisButtonTextRect )

# draws the button to run the GA on the menu
def drawRunGAButton():
    global runGAButtonRect

    xPos = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPos = SCREEN_HEIGHT / 4 + SCREEN_PADDING + ( 1 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 1 * BUTTON_PADDING_SIZE )

    runGAButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    runGAButtonText = BUTTON_FONT.render( "Run Genetic Algorithm", True, WHITE )
    runGAButtonTextRect = runGAButtonText.get_rect( center = ( ( xPos + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( runGAButtonText, runGAButtonTextRect )

# draws the button for the settings on the menu for the genetic algorithm
def drawGASettingsButton():
    global settingsButtonRect

    xPos = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPos = SCREEN_HEIGHT / 4 + SCREEN_PADDING + ( 2 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 2 * BUTTON_PADDING_SIZE )

    settingsButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    settingsButtonText = BUTTON_FONT.render( "Genetic Algorithm Settings", True, WHITE )
    settingsButtonTextRect = settingsButtonText.get_rect( center = ( ( xPos + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( settingsButtonText, settingsButtonTextRect )

# draws the buttons for the wisdom of crowds control to enable or disable the WOC
def drawWisdomOfCrowdsButton():
    global wisdomOfCrowdsButtonRect

    xPos = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPos = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 0 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 0 * BUTTON_PADDING_SIZE )

    wisdomOfCrowdsButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    wisdomOfCrowdsButtonText = BUTTON_FONT.render( "Wisdom Of Crowds (Disabled)", True, WHITE )
    if Parameters.wisdomOfCrowds == True:
        wisdomOfCrowdsButtonText = BUTTON_FONT.render( "Wisdom Of Crowds (Enabled)", True, WHITE )
    wisdomOfCrowdsButtonTextRect = wisdomOfCrowdsButtonText.get_rect( center = ( ( xPos + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( wisdomOfCrowdsButtonText, wisdomOfCrowdsButtonTextRect )

# Summary: draws the components associated with the wisdom of crowds rate control
def drawWisdomOfCrowdsRateControls():
    global wisdomOfCrowdsMinusButtonRect
    global wisdomOfCrowdsPlusButtonRect


    xPosWisdomOfCrowdsText = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosWisdomOfCrowdsText = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 1 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 1 * BUTTON_PADDING_SIZE ) - 10

    wisdomOfCrowdsText = BUTTON_FONT.render( f"Wisdom Of Crowds Generations: {Parameters.wisdomOfCrowdsGenerations}", True, WHITE )
    wisdomOfCrowdsTextRect = wisdomOfCrowdsText.get_rect( center = ( ( xPosWisdomOfCrowdsText + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPosWisdomOfCrowdsText + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( wisdomOfCrowdsText, wisdomOfCrowdsTextRect )

    xPosWisdomOfCrowdsButtons = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosWisdomOfCrowdsButtons = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 1 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 3 * BUTTON_PADDING_SIZE ) - 10

    wisdomOfCrowdsMinusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosWisdomOfCrowdsButtons, yPosWisdomOfCrowdsButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )
    wisdomOfCrowdsPlusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosWisdomOfCrowdsButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE, yPosWisdomOfCrowdsButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )

    # Adds the text to the button in the middle of the button
    wisdomOfCrowdsMinusButtonText = BUTTON_FONT.render( "- 5", True, WHITE )
    wisdomOfCrowdsMinusButtonTextRect = wisdomOfCrowdsMinusButtonText.get_rect( center = ( ( xPosWisdomOfCrowdsButtons + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosWisdomOfCrowdsButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( wisdomOfCrowdsMinusButtonText, wisdomOfCrowdsMinusButtonTextRect )

    wisdomOfCrowdsPlusButtonText = BUTTON_FONT.render( "+ 5", True, WHITE )
    wisdomOfCrowdsPlusButtonTextRect = wisdomOfCrowdsPlusButtonText.get_rect( center = ( ( xPosWisdomOfCrowdsButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosWisdomOfCrowdsButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( wisdomOfCrowdsPlusButtonText, wisdomOfCrowdsPlusButtonTextRect )

# Summary: draws the components associated with the population size control
def drawPopulationSizeControls():
    global populationSizeMinusButtonRect
    global populationSizePlusButtonRect


    xPosPopulationText = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosPopulationText = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 3 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 1 * BUTTON_PADDING_SIZE )

    populationSizeText = BUTTON_FONT.render( f"Population Size: {Parameters.populationSize}", True, WHITE )
    populationSizeTextRect = populationSizeText.get_rect( center = ( ( xPosPopulationText + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPosPopulationText + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( populationSizeText, populationSizeTextRect )

    xPosPopulationButtons = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosPopulationButtons = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 3 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 3 * BUTTON_PADDING_SIZE )

    populationSizeMinusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosPopulationButtons, yPosPopulationButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )
    populationSizePlusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosPopulationButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE, yPosPopulationButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )

    # Adds the text to the button in the middle of the button
    populationSizeMinusButtonText = BUTTON_FONT.render( "- 5", True, WHITE )
    populationSizeMinusButtonTextRect = populationSizeMinusButtonText.get_rect( center = ( ( xPosPopulationButtons + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosPopulationButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( populationSizeMinusButtonText, populationSizeMinusButtonTextRect )

    populationSizePlusButtonText = BUTTON_FONT.render( "+ 5", True, WHITE )
    populationSizePlusButtonTextRect = populationSizePlusButtonText.get_rect( center = ( ( xPosPopulationButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosPopulationButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( populationSizePlusButtonText, populationSizePlusButtonTextRect )

# Summary: draws the components associated with the mutation rate control
def drawMutationRateControls():
    global mutationRateMinusButtonRect
    global mutationRatePlusButtonRect

    xPosMutationRateText = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosMutationRateText = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 4 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 3 * BUTTON_PADDING_SIZE ) + 10

    mutationRateText = BUTTON_FONT.render( f"Mutation Rate: {Parameters.mutationRate:.2f}", True, WHITE )
    mutationRateTextRect = mutationRateText.get_rect( center = ( ( xPosMutationRateText + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPosMutationRateText + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( mutationRateText, mutationRateTextRect )

    xPosMutationRateButtons = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPosMutationRateButtons = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 4 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 5 * BUTTON_PADDING_SIZE ) + 10

    mutationRateMinusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosMutationRateButtons, yPosMutationRateButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )
    mutationRatePlusButtonRect = pygame.draw.rect( screen, BLUE, ( xPosMutationRateButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE, yPosMutationRateButtons, HALF_SIZE_BUTTON_SIZE_X, HALF_SIZE_BUTTON_SIZE_Y ) )

    # Adds the text to the button in the middle of the button
    mutationRateMinusButtonText = BUTTON_FONT.render( "- .05", True, WHITE )
    mutationRateMinusButtonTextRect = mutationRateMinusButtonText.get_rect( center = ( ( xPosMutationRateButtons + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosMutationRateButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( mutationRateMinusButtonText, mutationRateMinusButtonTextRect )

    mutationRatePlusButtonText = BUTTON_FONT.render( "+ .05", True, WHITE )
    mutationRatePlusButtonTextRect = mutationRatePlusButtonText.get_rect( center = ( ( xPosMutationRateButtons + HALF_SIZE_BUTTON_SIZE_X + BUTTON_PADDING_SIZE + HALF_SIZE_BUTTON_SIZE_X / 2 ), yPosMutationRateButtons + ( HALF_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( mutationRatePlusButtonText, mutationRatePlusButtonTextRect )

# Draws the back button for the settings to get back to the menu
def drawSettingsBackButton():
    global settingsBackButtonRect

    xPos = SCREEN_WIDTH / 2 - FULL_SIZE_BUTTON_SIZE_X / 2
    yPos = SCREEN_HEIGHT / 6 + SCREEN_PADDING + ( 8 * FULL_SIZE_BUTTON_SIZE_Y ) + ( 1 * BUTTON_PADDING_SIZE )

    settingsBackButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    backButtonText = BUTTON_FONT.render( "Back to Menu", True, WHITE )
    backButtonTextRect = backButtonText.get_rect( center = ( ( xPos + FULL_SIZE_BUTTON_SIZE_X / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( backButtonText, backButtonTextRect )

# draws the replay button to allow the game to be replayed
def drawReplayButton():
    global replayButtonRect

    xPos = 400
    yPos = SCREEN_HEIGHT - SCREEN_PADDING - BUTTON_PADDING_SIZE - FULL_SIZE_BUTTON_SIZE_Y - 2

    replayButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X * .75, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    replayButtonText = BUTTON_FONT.render( "Restart Game", True, WHITE )
    replayButtonTextRect = replayButtonText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( replayButtonText, replayButtonTextRect )

# Draws the back button for the game to go from tetris to the main menu
def drawTetrisBackButton():
    global tetrisBackButtonRect

    xPos = 400
    yPos = SCREEN_HEIGHT - SCREEN_PADDING - 2 * BUTTON_PADDING_SIZE - 2 * FULL_SIZE_BUTTON_SIZE_Y - 2

    tetrisBackButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X * .75, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    backButtonText = BUTTON_FONT.render( "Back to Menu", True, WHITE )
    backButtonTextRect = backButtonText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( backButtonText, backButtonTextRect )

# draws the back button to go from the GA to the menu
def drawGABackButton():
    global gaBackButtonRect

    xPos = 400
    yPos = SCREEN_HEIGHT - SCREEN_PADDING - BUTTON_PADDING_SIZE - FULL_SIZE_BUTTON_SIZE_Y - 2

    gaBackButtonRect = pygame.draw.rect( screen, BLUE, ( xPos, yPos, FULL_SIZE_BUTTON_SIZE_X * .75, FULL_SIZE_BUTTON_SIZE_Y ) )
    
    # Adds the text to the button in the middle of the button
    backButtonText = BUTTON_FONT.render( "Back to Menu", True, WHITE )
    backButtonTextRect = backButtonText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( backButtonText, backButtonTextRect )

# given a score, it prints it to the screen
def drawScore( score ):
    xPos = 400
    yPos = SCREEN_PADDING + BUTTON_PADDING_SIZE

    # Adds the text to the button in the middle of the button
    scoreText = SCORE_FONT.render( f"Game Score: {score}", True, WHITE )
    scoreTextRect = scoreText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( scoreText, scoreTextRect )

# given a fitness score, it draws it to the screen
def drawFitnessScore( score ):
    xPos = 400
    yPos = SCREEN_PADDING + 3 * BUTTON_PADDING_SIZE

    # Adds the text to the button in the middle of the button
    scoreText = SCORE_FONT.render( f"Fitness Score: {score}", True, WHITE )
    scoreTextRect = scoreText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( scoreText, scoreTextRect )

# draws the generation number to the screen
def drawGenerationNumber( generationNumber ):
    xPos = 400
    yPos = SCREEN_PADDING + 7 * BUTTON_PADDING_SIZE

    # Adds the text to the button in the middle of the button
    generationText = SCORE_FONT.render( f"Generation: {generationNumber}", True, WHITE )
    generationTextRect = generationText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( generationText, generationTextRect )

# draws the number of rows cleared to the screen
def drawRowsCleared( numRowsCleared ):
    xPos = 400
    yPos = SCREEN_PADDING + 5 * BUTTON_PADDING_SIZE

    # Adds the text to the button in the middle of the button
    rowsText = SCORE_FONT.render( f"Rows Cleared: {numRowsCleared}", True, WHITE )
    rowsTextRect = rowsText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( rowsText, rowsTextRect )

# draws the next block to the screen
def drawNextBlock( block ):
    xPos = 400
    yPos = SCREEN_PADDING + 10 * BUTTON_PADDING_SIZE

    nextBlockText = SCORE_FONT.render( "Next Block:", True, WHITE )
    nextBlockTextRect = nextBlockText.get_rect( center = ( ( xPos + ( FULL_SIZE_BUTTON_SIZE_X * .75 ) / 2 ), yPos + ( FULL_SIZE_BUTTON_SIZE_Y / 2 ) ) )
    screen.blit( nextBlockText, nextBlockTextRect )
    block.draw( screen, xPos, yPos + 60 )
    
# handles the events of the program based on the current running state
def handleEvents():
    if Parameters.runningState == 0:
        handleMenuEvents()
    if Parameters.runningState == 1:
        handleSettingsEvents()
    if Parameters.runningState == 2:
        handleTetrisEvents()
    if Parameters.runningState == 3:
        handleGAEvents()
    if Parameters.runningState == 4:
        handleWOC()
    elif Parameters.wisdomOfCrowdsGenerations == len(Parameters.gen_algs_best_agents) and Parameters.gottowoc == False:
        handleWOCEvents()

def handleWOC():
    gaAgent = WOCAlg.bestAgent
    for event in pygame.event.get():
        if event.type == game_update and gaAgent.gameOver == False:
            nextMove = gaAgent.getNextMove()
            if nextMove == "NOTHING":
                pass
            if nextMove == "LEFT":
                gaAgent.moveLeft()
            if nextMove == "RIGHT":
                gaAgent.moveRight()
            if nextMove == "UP":
                gaAgent.rotate()
            gaAgent.moveDown()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Summary: the loop to handle the prerunning pygame events such as any of the button presses
def handleMenuEvents():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if ga button pressed, run the ga
            if runGAButtonRect.collidepoint( event.pos ):
                Parameters.runningState = 3
            # if the play button is pressed, run tetris
            if playTetrisButtonRect.collidepoint( event.pos ):
                Parameters.runningState = 2
            # if the settings button is pressed, go to settings
            if settingsButtonRect.collidepoint( event.pos ):
                Parameters.runningState = 1
        # if the event is quit, stop running
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Summary: the loop to handle the running pygame events such as any of the button presses
def handleSettingsEvents():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if wisdom of crowds button pressed, enable or disable wisdom of crowds
            if wisdomOfCrowdsButtonRect.collidepoint( event.pos ):
                Parameters.wisdomOfCrowds = not Parameters.wisdomOfCrowds
            # if the minus wisdom of crowds rate button is clicked, adjust wisdom of crowds rate
            if wisdomOfCrowdsMinusButtonRect.collidepoint( event.pos ):
                if Parameters.wisdomOfCrowdsGenerations - 5 >= 0.01:
                    Parameters.wisdomOfCrowdsGenerations = Parameters.wisdomOfCrowdsGenerations - 5
            # if the plus wisdom of crowds rate button is clicked, adjust wisdom of crowds rate
            if wisdomOfCrowdsPlusButtonRect.collidepoint( event.pos ):
                Parameters.wisdomOfCrowdsGenerations = Parameters.wisdomOfCrowdsGenerations + 5
            # if the minus population button is clicked, adjust population size
            if populationSizeMinusButtonRect.collidepoint( event.pos ):
                if Parameters.populationSize - 5 >= 5:
                    Parameters.populationSize = Parameters.populationSize - 5
            # if the plus population button is clicked, adjust population size
            if populationSizePlusButtonRect.collidepoint( event.pos ):
                Parameters.populationSize = Parameters.populationSize + 5
            # if the minus mutation rate button is clicked, adjust mutation rate
            if mutationRateMinusButtonRect.collidepoint( event.pos ):
                if Parameters.mutationRate - .05 >= 0:
                    Parameters.mutationRate = Parameters.mutationRate - .05
            # if the plus mutation rate button is clicked, adjust mutation rate
            if mutationRatePlusButtonRect.collidepoint( event.pos ):
                if Parameters.mutationRate + .05 <= 1.01:
                    Parameters.mutationRate = Parameters.mutationRate + .05
            # if back button is clicked, put into running state 0
            if settingsBackButtonRect.collidepoint( event.pos ):
                Parameters.runningState = 0
        # if the event is quit, stop running
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# event handler for the events which happen in running the tetris game
def handleTetrisEvents():
    for event in pygame.event.get():
        # if the clock ticks, move the game down
        if event.type == game_update and game.gameOver == False:
            game.moveDown()
        # if the event is a click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if it is replay button, restart the game
            if replayButtonRect.collidepoint( event.pos ):
                game.gameOver = False
                game.newGame()
            # if it is back button, navigate to the menu
            if tetrisBackButtonRect.collidepoint( event.pos ):
                game.gameOver = False
                game.newGame()
                Parameters.runningState = 0
        # if the event is a key press
        if event.type == pygame.KEYDOWN:
            # if the left key is pressed, move left
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            # if the right key is pressed, move right
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            # if the down key is pressed, move the game down
            if event.key == pygame.K_DOWN and game.gameOver == False:
                game.moveDown()
                game.updateScore( 0, 1 )
            # if the up key is pressed, rotate the piece
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotate()
                
        # if the event is quit, stop running
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def handleGAEvents():
    global bestAgent
    # for each of the events
    for event in pygame.event.get():
        # if the mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the back button is clicked, reset the ga
            if gaBackButtonRect.collidepoint( event.pos ):
                TetrisGA.resetGA()
                Parameters.runningState = 0
        # if the event is quit, stop running
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # for each agent in the population
    for gaAgent in TetrisGA.population:
        # as long as the game is not over
        if gaAgent.gameOver == False:
            # get the next move
            nextMove = gaAgent.getNextMove()
            # depending on the move, move the block accordingly
            if nextMove == "NOTHING":
                pass
            if nextMove == "LEFT":
                gaAgent.moveLeft()
            if nextMove == "RIGHT":
                gaAgent.moveRight()
            if nextMove == "UP":
                gaAgent.rotate()
            # move the game down no matter what
            gaAgent.moveDown()
    # get the best agent
    bestAgent = TetrisGA.getBestAgent()
    # If the generation is no longer running
    if TetrisGA.getIsGenerationRunning() == False:
        # if the number of generations is equal to the max generations set in parameters, run the algorithm again
        if Parameters.numGenerations == TetrisGA.generation:
            TetrisGA.resetGA()
            return
        # otherwise get the next generation
        TetrisGA.getNextGen()

def handleWOCEvents():
    global WOCAlg 
    WOCAlg = WOCGenAlg()