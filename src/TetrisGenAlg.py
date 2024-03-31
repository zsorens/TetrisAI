import Parameters
import random
import Mutations
import copy 
from GAAgent import GAAgent

class TetrisGenAlg:
    def __init__( self ): # init object for one iteration of the genetic algorithm
        self.blockList = self.getBlockList()
        self.generation = 0
        self.population = self.initializePopulation()
        self.isGenerationRunning = True
        self.bestAgent = None
        self.bestFitness = 0

    def getBlockList( self ): # get block list for one iteration of the genetic algorithm, for the first iteration, set the whole projects block list to this one
        availableBlocks = [ "IBlock", "JBlock", "LBlock", "OBlock", "SBlock", "TBlock", "ZBlock" ]
        blockList = []
        for i in range( Parameters.numBlocks ):
            if len( availableBlocks ) == 0:
                availableBlocks = [ "IBlock", "JBlock", "LBlock", "OBlock", "SBlock", "TBlock", "ZBlock" ]
            block = random.choice( availableBlocks )
            blockList.append( block )
            availableBlocks.remove( block )
        Parameters.blockList = blockList
        return blockList
    
    def initializePopulation( self ): # create starter population
        population = []
        for i in range( Parameters.populationSize ):
            population.append( GAAgent( self.blockList ) )

        self.generation += 1
        return population
    
    def getIsGenerationRunning( self ): # check bool for if the generation is running 
        for gaAgent in self.population:
            if gaAgent.gameOver == False:
                self.isGenerationRunning = True
                return True
        self.isGenerationRunning = False
        return False

    def getBestAgent( self ): # find the best population member, based on fitienss score
        bestFitness = 0
        bestAgent = None
        for gaAgent in self.population:
            if gaAgent.fitnessScore >= bestFitness:
                bestFitness = gaAgent.fitnessScore
                bestAgent = gaAgent
        self.bestAgent = bestAgent
        self.bestFitness = bestFitness
        return bestAgent
    
    def resetGA( self ): # reset the GA for the next iteration for WOC
        Parameters.gen_algs_best_agents.append(self.bestAgent)
        self.blockList = Parameters.blockList
        self.generation = 0
        self.population = self.initializePopulation()
        self.isGenerationRunning = True
        self.bestAgent = None
        self.bestFitness = 0

    def getNextGen( self ): # create the next generation by using crossovers and mutations
        nextgen = []

        for i in range( int( Parameters.populationSize / 2 ) ):
            parent1, parent2 = self.selectParents()

            parent1Moves = parent1.moves
            parent1MoveCounter = parent1.moveCounter
            parent2Moves = parent2.moves
            parent2MoveCounter = parent2.moveCounter


            moveCounter = 0
            if parent1MoveCounter > parent2MoveCounter:
                moveCounter = parent1MoveCounter
            else:
                moveCounter = parent2MoveCounter

            child1Moves, child2Moves = Mutations.point_crossover( parent1Moves, parent2Moves, moveCounter )
            if random.random() < Parameters.mutationRate:
                child1Moves = Mutations.swap_mutation( child1Moves, moveCounter )
            if random.random() < Parameters.mutationRate:
                child2Moves = Mutations.swap_mutation( child2Moves, moveCounter )


            nextgen.append( GAAgent( self.blockList, child1Moves ) )
            nextgen.append( GAAgent( self.blockList, child2Moves ) )

        if len( nextgen ) == ( Parameters.populationSize + 1 ):
            nextgen.pop( len( nextgen ) - 1 )

        self.isGenerationRunning = True
        self.generation += 1
        self.population = nextgen
    
    # Summary: select two parents and return them to mate with each other
    def selectParents( self ):
        selectedParents = self.tournamentSelection()
        return selectedParents[ 0 ], selectedParents[ 1 ]

    # Summary: selects two parents using tournament-based selection
    def tournamentSelection( self ):
        # initialize the array to hold the parents
        selectedParents = []

        # loop twice to generate two parents
        while len( selectedParents ) < 2:
            # initialize the tournament to be an array of positions of size tournamentSize
            tournament = random.sample( range( Parameters.populationSize ), Parameters.tournamentSize )
        
            # select the best parent by looping through each of the positions and select the one with highest fitness
            bestCandidate = tournament[ 0 ]
            for candidate in tournament:
                if self.population[ candidate ].fitnessScore > self.population[ bestCandidate ].fitnessScore:
                    bestCandidate = candidate

            # add the best candidate to the parent array
            selectedParents.append( self.population[ bestCandidate ] )

        # return the two parents
        return selectedParents
