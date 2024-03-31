import Parameters as p 
from collections import Counter as c 
from GAAgent import GAAgent

#initialize our class up top
class WOCGenAlg:

    #we start by initializing a bunch of our parameters and setting our default values.
    def __init__( self ):
        p.runningState = 4
        p.gottowoc = True
        self.genAlgs = p.gen_algs_best_agents
        self.bestAgent =  0 
        self.findBestAgent()

    def findBestAgent( self ):
        full_list = []      #Declare two empty lists in our function
        result_list = []
        # for agent in self.genAlgs:
        #     full_list.append(agent.moves)
        # for vals in zip(*full_list):
        #     freq = c(vals)
        #     most_seen_vals, _ = freq.most_common(1)[0]
        #     result_list.append(most_seen_vals)
        # self.bestAgent = GAAgent(p.blockList, result_list)
        # p.best_agent = self.bestAgent

        for agent in self.genAlgs: #create a for loop here to iterate through self.genAlgs
            if agent.rowsCleared > 1: #if our rows cleared is greater than 1 append the moves to our list.
                full_list.append(agent.moves)

        for vals in zip(*full_list): #transpose the whole list here using zip and will calculate the most common value for each position using our counter
            freq = c(vals)
            most_seen_vals, _ = freq.most_common(1)[0]
            result_list.append(most_seen_vals)
        self.bestAgent = GAAgent(p.blockList, result_list) #create a new GAAgent here and update the current best agent.
        p.best_agent = self.bestAgent #reassing the best agent.
