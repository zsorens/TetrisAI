import numpy as np 

#we have a main tetris function which calls the WOC process function
def main_tetris():
    WOCProcess()



def WOCProcess(moves = []):
    for i in 25:
        aggergation(moves)

def aggergation(moves = []):
    print('Got here')

def mutation(moves = []):
    temp = []
    for i in len(moves):
        if(i < len(moves) / 2):
            temp.append(moves[i])
            moves.remove(moves[i])
    temp.append(moves)

def selection(moves = []):
    if(np.random()):
        print(y)


