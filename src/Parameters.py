# GA parameters
populationSize = 10
mutationRate = .3

# running state 0 = menu, running state 1 = GA settings, running state 2 = running tetris, running state 3 = GA
runningState = 0

# Not sure if we will need these atm depending on parent selection alg / woc alg
tournamentSize = 10
wisdomOfCrowds = True
wisdomOfCrowdsGenerations = 5

# For number of moves a GAAgent can have
numBlocks = 100
numMoves = numBlocks * 20

# Moves the GAAgent can make
moves = [ "NOTHING", "LEFT", "RIGHT", "UP" ]

#initialize our empty arrays and set our number of generations we will run through.
numGenerations = 10
gen_algs_best_agents = []
blockList = []

#intilize boolean to flag if we get to wisdom of crowds and also intialize our best agent to none.
gottowoc = False
best_agent = None